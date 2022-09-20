import contextlib
import inspect
import io

def decorator_2(func):
    def wrapper(*args, **kwargs):
        print(f'Name: \t{func.__name__}')
        print(f'Type: \t{str(type(func))}')
        print(f'Sign: \t{inspect.signature(func)}')
        print(f'Args: \tpositional {args}')
        print(f'      \tkey-worded {kwargs}\n')

        print(f'Doc: \t{func.__doc__}\n')
        print(f'Source:', end='')
        i = 0
        for line in inspect.getsourcelines(func)[0]:
            print((' ' + line if i == 0 else '\t' + line), end='')
            i += 1

        print(f'\nOutput:')
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)
        s = f.getvalue()
        for line in s.splitlines():
            print(f'\t{line}', end='\n')
    return wrapper