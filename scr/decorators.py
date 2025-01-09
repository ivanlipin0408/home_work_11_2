from datetime import datetime
from pathlib import Path
from functools import wraps
from typing import Callable, Any
from mypy.util import os_path_join

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir/"data"/"mylog.txt"

def log(filename = None):
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = my_function(*args, **kwargs)
                log_result = "my_function ok"

            except Exception as e:
                log_result = f"my_function error: {str(e)}. Inputs: ({args}"

            finally:
                end_time = datetime.now()
                log_result += f"Time:{end_time - start_time}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_result + "\n")
                else:
                    print(log_result)
            return log_result
        return wrapper
    return logging


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

