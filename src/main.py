import random
from task1 import decorator_1
from task2 import decorator_2
import task3

def quadratic_solver(eq):
    return eq

def pascal_triangle(n):
    print(n)

# @decorator_1
# @decorator_2
@task3.decorator_3
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        

# @decorator_1
# @decorator_2
@task3.decorator_3
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
    # func()
    # func()
    # funx()
    # func()

    print(f'PROGRAM | RANK | TIME ELAPSED')
    functions_rank = task3.rank
    for i, (k, v) in enumerate(sorted(functions_rank.items(), key=lambda item: item[1])):
        print(f'{k}: \t{i + 1} \t{v}')



