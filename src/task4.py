import contextlib
import inspect
import time
import io


functions_data = {}
rank = {}

class decorator_4():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        global functions_data
        global rank

        with open('files/logs.txt', 'a') as logs_file:
            with contextlib.redirect_stderr(logs_file):
                try:
                    with open('files/output.txt', 'a') as f:
                        with contextlib.redirect_stdout(f):

                            func_result = io.StringIO()
                            with contextlib.redirect_stdout(func_result):
                                begin = time.time()
                                result = self.func(*args, **kwargs)
                                end = time.time()
                            execution_time = end - begin
                            if functions_data.get(self.func.__name__) is None:
                                functions_data[self.func.__name__] = 1
                            else:
                                functions_data[self.func.__name__] += 1
                            print(f'{self.func.__name__} call {functions_data[self.func.__name__]} executed in {execution_time:.6f} sec')


                            print(f'Name: \t{self.func.__name__}')
                            print(f'Type: \t{str(type(self.func))}')
                            print(f'Sign: \t{inspect.signature(self.func)}')
                            print(f'Args: \tpositional {args}')
                            print(f'      \tkey-worded {kwargs}\n')

                            print(f'Doc: \t{self.func.__doc__}\n')
                            print(f'Source:', end='')
                            i = 0
                            for line in inspect.getsourcelines(self.func)[0]:
                                print((' ' + line if i == 0 else '\t' + line), end='')
                                i += 1

                            print(f'\nOutput:')
                            f = io.StringIO()
                            with contextlib.redirect_stdout(f):
                                result = self.func(*args, **kwargs)
                            s = f.getvalue()
                            for line in s.splitlines():
                                print(f'\t{line}', end='\n')

                            rank[self.func.__name__] = f'{execution_time:.9f} s'
                            return result
                except BaseException as err:
                    print(f'Oops!  That was an error: {err}')

