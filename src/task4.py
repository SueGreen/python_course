import contextlib
import inspect
import time
import datetime
import io
from pathlib import Path


rank = {}
num_calls = {}
functions_statistics = {'name': [], 'call_number': [], 'execution_time': []}

class decorator_4():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        # with open('files/logs.txt', 'a+') as logs_file:
        #     with contextlib.redirect_stderr(logs_file):
        with open('files/logs.txt', 'a+') as logs_file, contextlib.redirect_stderr(logs_file):
        # with open('filename.log', 'w') as stderr, contextlib.redirect_stderr(stderr):
        #     print(1/0)    # errors from here are logged to the file.
            print(9 / 0)
            # try:
            #     print(9 / 0)
                # try:
                #     print(9 / 0)
                    
                    # with open(Path('files/output.txt'), 'a+') as output_file:
                    #     with contextlib.redirect_stdout(output_file):

                    #         func_result_dump = io.StringIO()
                    #         with contextlib.redirect_stdout(func_result_dump):
                    #             begin = time.time()
                    #             result = self.func(*args, **kwargs)
                    #             end = time.time()
                    #         execution_time = end - begin
                    #         if num_calls.get(self.func.__name__) is None:
                    #             num_calls[self.func.__name__] = 1
                    #             call_number = num_calls[self.func.__name__]
                    #         else:
                    #             num_calls[self.func.__name__] += 1
                    #             call_number = num_calls[self.func.__name__]
                    #         functions_statistics['name'].append(self.func.__name__)
                    #         functions_statistics['call_number'].append(call_number)
                    #         functions_statistics['execution_time'].append(execution_time)
                    #         print(f'{self.func.__name__} call {call_number} executed in {execution_time:.6f} sec')


                    #         print(f'Name: \t{self.func.__name__}')
                    #         print(f'Type: \t{str(type(self.func))}')
                    #         print(f'Sign: \t{inspect.signature(self.func)}')
                    #         print(f'Args: \tpositional {args}')
                    #         print(f'      \tkey-worded {kwargs}\n')

                    #         print(f'Doc: \t{self.func.__doc__}\n')
                    #         print(f'Source:', end='')
                    #         i = 0
                    #         for line in inspect.getsourcelines(self.func)[0]:
                    #             print((' ' + line if i == 0 else '\t' + line), end='')
                    #             i += 1

                    #         print(f'\nOutput:')
                    #         s = func_result_dump.getvalue()
                    #         for line in s.splitlines():
                    #             print(f'\t{line}', end='\n')

                    #         rank[self.func.__name__] = f'{execution_time:.9f} s'
                    #         return result
            # except BaseException as err:
            #         print(f'{str(datetime.datetime.now())}'
            #             f'{time.time()} \nAn error occured: {err}\n')  
                # except BaseException as err:
                #     print(f'{str(datetime.datetime.now())}'
                #         f'{time.time()} \nAn error occured: {err}\n')

