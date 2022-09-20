import random
import cmath
import pandas as pd
from IPython.display import display
from task1 import decorator_1
from task2 import decorator_2
import task3
import task4



reverse_upper = lambda a_string: a_string.upper()[::-1]

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age >= 18, ages))


# @decorator_1
# @decorator_2
# @task3.decorator_3
@task4.decorator_4
def quadratic_solver(a=1,b=4, c=2): 
    discriminant = (b**2) - (4 * a * c)
    ans1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    ans2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    print(f'roots are: {ans1}, {ans2}')

# @decorator_1
# @decorator_2
# @task3.decorator_3
@task4.decorator_4
def pascal_triangle(n):
    cur = [1]
    for row_num in range(n):
        new = [1]
        for elem_num in range(len(cur)-1):
            new.append(cur[elem_num] + cur[elem_num + 1])
        new = new + [1]
        print(*new)
        cur = new

# @decorator_1
# @decorator_2
# @task3.decorator_3
@task4.decorator_4
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        

# @decorator_1
# @decorator_2
# @task3.decorator_3
@task4.decorator_4
def funx(n=2, m=5):
    '''DoCstring'''
    print('I am ready to \ndo serious stuff')
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    
    func()
    funx(2, 3)
    func()
    func()
    funx()
    func()
    # quadratic_solver(1, 4, 2)
    # pascal_triangle(5)

    print(f'Information about last execution:')
    print(f'PROGRAM | RANK | TIME ELAPSED')
    if task4.functions_statistics is not None:
        last_execution_statistics = task4.rank
        full_functions_statistics = task4.functions_statistics
    else:
        functions_data = task3.num_calls 

    for i, (k, v) in enumerate(sorted(last_execution_statistics.items(), key=lambda item: item[1])):
        print(f'{k}: \t{i + 1} \t{v}')

    
    print(f'\nMore detailed information:')
    if full_functions_statistics is not None:
        full_functions_statistics = pd.DataFrame(full_functions_statistics)
        display(full_functions_statistics.groupby('name', as_index=False).agg(
            mean_execution_time=('execution_time', 'mean'),
            min_execution_time=('execution_time', 'min'),
            max_execution_time=('execution_time', 'max'),
            calls_num=('call_number', 'max')
        ).sort_values(by='mean_execution_time').reset_index(drop=True))



