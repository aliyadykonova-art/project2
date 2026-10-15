"""Точка входа в программу обработки банковских транзакций."""

from typing import Any, Callable

from src.processing import (
    filter_by_state,
    process_bank_search,
    sort_by_date,
)
from src.utils import (
    read_json_file,
    read_transactions_from_csv,
    read_transactions_from_excel,
)


def load_transactions() -> list[dict[str, Any]]:
    """Предлагает формат файла и загружает транзакции."""
    file_options: dict[str, tuple[str, Callable, str]] = {
        "1": ("JSON", read_json_file, "data/operations.json"),
        "2": ("CSV", read_transactions_from_csv, "data/transactions.csv"),
        "3": (
            "XLSX",
            read_transactions_from_excel,
            "data/transactions_excel.xlsx",
        ),
    }

    print("Выберите формат файла:")
    print("1. JSON")
    print("2. CSV")
    print("3. XLSX")

    while True:
        choice = input("Ваш выбор: ").strip()

        if choice in file_options:
            name, loader, path = file_options[choice]
            print(f"Загрузка данных из {name}...")
            try:
                return loader(path)
            except (OSError, ValueError, ImportError) as error:
                print(f"Ошибка загрузки файла: {error}")
                return []

        print("Неверный выбор. Введите 1, 2 или 3.")


def get_currency(operation: dict[str, Any]) -> str:
    """Получает код валюты операции из поддерживаемых форматов."""
    currency_code = operation.get("currency_code")

    if currency_code:
        return str(currency_code).upper()

    for key in ("operationAmount", "operation", "amount_data"):
        amount_data = operation.get(key)

        if isinstance(amount_data, dict):
            currency = amount_data.get("currency", {})

            if isinstance(currency, dict) and currency.get("code"):
                return str(currency["code"]).upper()

    currency = operation.get("currency", "")

    if isinstance(currency, dict):
        currency = currency.get("code", "")

    return str(currency).upper()


def is_ruble_operation(operation: dict[str, Any]) -> bool:
    """Проверяет, что валюта операции — российский рубль."""
    return get_currency(operation) in {"RUB", "RUR"}


def format_operation(operation: dict[str, Any]) -> str:
    """Формирует текстовое представление банковской операции."""
    date = str(operation.get("date", operation.get("Дата", "")))[:10]
    description = operation.get(
        "description",
        operation.get("Описание", "Без описания"),
    )

    amount_data = operation.get("operationAmount")

    if isinstance(amount_data, dict):
        amount = amount_data.get("amount", "")
        currency_data = amount_data.get("currency", {})

        if isinstance(currency_data, dict):
            currency = currency_data.get(
                "name",
                currency_data.get("code", ""),
            )
        else:
            currency = currency_data
    else:
        amount = operation.get("amount", operation.get("Сумма", ""))
        currency = operation.get(
            "currency_name",
            operation.get("currency_code", ""),
        )

    sender = operation.get("from", operation.get("Откуда", ""))
    recipient = operation.get("to", operation.get("Куда", ""))

    if sender is None:
        sender = ""
    if recipient is None:
        recipient = ""

    result = (
        f"{date} {description}\n"
        f"Сумма: {amount} {currency}"
    )

    if sender or recipient:
        result += (
            f"\n{sender or 'Не указан'} -> "
            f"{recipient or 'Не указан'}"
        )

    return result


def ask_yes_no(question: str) -> bool:
    """Запрашивает у пользователя ответ да или нет."""
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()

        if answer in {"да", "д", "yes", "y"}:
            return True

        if answer in {"нет", "н", "no", "n"}:
            return False

        print("Пожалуйста, ответьте да или нет.")


def choose_state() -> str:
    """Запрашивает статус операций."""
    states = {
        "1": "EXECUTED",
        "2": "CANCELED",
        "3": "PENDING",
    }

    print("\nВыберите статус операции:")
    print("1. EXECUTED — выполнена")
    print("2. CANCELED — отменена")
    print("3. PENDING — ожидает обработки")

    while True:
        choice = input("Ваш выбор: ").strip()

        if choice in states:
            return states[choice]

        print("Неверный выбор. Введите 1, 2 или 3.")


def main() -> None:
    """Запускает интерактивную обработку банковских транзакций."""
    operations = load_transactions()

    if not operations:
        print("Не удалось загрузить транзакции или файл пуст.")
        return

    state = choose_state()
    operations = filter_by_state(operations, state)

    if ask_yes_no("Отсортировать операции по дате?"):
        descending = ask_yes_no(
            "Сначала показывать самые новые операции?"
        )
        operations = sort_by_date(operations, reverse=descending)

    if ask_yes_no("Выводить только операции в рублях?"):
        operations = [
            operation
            for operation in operations
            if is_ruble_operation(operation)
        ]

    if ask_yes_no("Искать операции по описанию?"):
        search = input(
            "Введите текст или регулярное выражение для поиска: "
        ).strip()

        if search:
            operations = process_bank_search(operations, search)

    if not operations:
        print(
            "\nНе найдено ни одной транзакции, "
            "подходящей под ваши условия."
        )
        return

    print(f"\nНайдено операций: {len(operations)}")
    print("Результаты обработки:")

    for operation in operations:
        print("-" * 40)
        print(format_operation(operation))

    print("-" * 40)


if __name__ == "__main__":
    main()
