from collections.abc import Callable
from functools import wraps


# логирует выполнение функции (в данном случае log это само название декоратора, и его аргументы)
def log(filename=None) -> Callable:
    """Декоратор для логирования функций в консоль и файл."""

    # получает саму функцию, к которой был применен декоратор.
    def decorator(func):
        # @wraps значит, что после применения декоратора, говорим ему что мы оставляем
        # оригинальные данные функции (такие, как docstring, и так далее)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # args - аргументы функции, к которой был применен декоратор.
                # kwargs - аргументы функции, которые были переданы через название параметра,
                # к которой был применен декоратор.
                result = func(*args, **kwargs)

                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
