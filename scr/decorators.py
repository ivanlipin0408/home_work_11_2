from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable

from mypy.util import os_path_join

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir / "data" / "mylog.txt"


def log(filename=None):
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_result = f"{func.__name__} ok. "

            except Exception as e:
                log_result = f"{func.__name__} error: {str(e)}. Inputs: ({args}"

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
