from functools import wraps
from pathlib import Path

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir / "data" / "mylog.txt"


def log(filename=None):
    """Функция логирует результат работы функции: указывает на успешное завершение или на ошибку с указанием
    аргументов функции"""

    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_result = f"{func.__name__} ok"

            except Exception as e:
                log_result = f"{func.__name__} error: {str(e)}. Inputs: {args}{kwargs}"

            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_result + "\n")
                else:
                    print(log_result)
            return log_result

        return wrapper

    return logging


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 2))
