# Учебный проект по Python

Проект для проверки банковских операций клиента. Написан на Python, зависимости управляются через Poetry.

## Что внутри


Три модуля в `src/`:

**`masks.py`** — маскировка номеров.
- `get_mask_card_number(card_number)` — принимает 16-значный номер карты, возвращает `7000 79** **** 6361`. На не-строку бросает `TypeError`, на строку не из 16 цифр — `ValueError`.
- `get_mask_account(card_number)` — принимает номер счёта, возвращает последние 4 цифры в виде `**4305`. Те же исключения: `TypeError` на не-строку, `ValueError` на нецифры или длину меньше 4.

**`widget.py`** — маскировка по строке с типом.
- `mask_account_card(info)` — принимает `"Visa Platinum 7000792289606361"` или `"Счет 73654108430135874305"`, возвращает строку с замаскированным номером. Распознаёт счёт по слову «счёт» в конце названия (регистр не важен).
- `get_date(date_str)` — превращает `"2019-07-03T18:35:29.512364"` в `"03.07.2019"`.

**`processing.py`** — фильтрация и сортировка операций.
- `filter_by_state(operations, state="EXECUTED")` — оставляет только операции с нужным статусом. На не-список бросает `TypeError`.
- `sort_by_date(operations, reverse=True)` — сортирует по дате. По умолчанию — от новых к старым.
- `get_date(op)` — достаёт дату из словаря операции. Если ключа нет — возвращает пустую строку. 

## Структура

```
PythonProject2/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── masks.py
│   ├── processing.py
│   └── widget.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── shell/
│   ├── check.sh
│   ├── init.sh
│   └── run.sh
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Установка

```bash
poetry install
```

Если Poetry ещё нет:

```bash
pip install poetry
poetry install
```

## Проверка кода

Из корня проекта:

```bash
poetry run flake8 .
poetry run isort .
poetry run mypy .
```

## Тесты

Тесты на pytest. Запуск:

```bash
poetry run pytest
```

Отдельный файл:

```bash
poetry run pytest tests/test_masks.py -v
```

По имени:

```bash
poetry run pytest -k "test_filter"
```


## Покрытие

Цель — не меньше 80%.

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

HTML-отчёт:

```bash
poetry run pytest --cov=src --cov-report=html
```





```bash
poetry run flake8 .
poetry run isort .
poetry run mypy .
poetry run pytest --cov=src
```