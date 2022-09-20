import time
import contextlib
import io

functions_data = {}


def decorator_1(func):
    def wrapper(*args, **kwargs):
        global functions_data

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            begin = time.time()
            result = func(*args, **kwargs)
            end = time.time()
        execution_time = end - begin

        if functions_data.get(func.__name__) is None:
            functions_data[func.__name__] = 1
        else:
            functions_data[func.__name__] += 1
        print(f'{func.__name__} call {functions_data[func.__name__]} executed in {execution_time:.6f} sec')
        return result

    return wrapper

