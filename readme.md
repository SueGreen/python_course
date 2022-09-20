# This is a set of exercises devoted to usage of decorators in Python

Let’s start by remembering the major characteristics of python programming language:

    High-level language
    Object-oriented language
    Functional language
    “Modular” language
    Dynamically typed language
    Interpreted language

In this assignment, we will try to exhaust all the characteristics of python. First, we start with number 4 (“Modular” language). Each task is implemented in a separate .py file and imported to the driver program in the main.py script with the following structure :

├── src              <- directory for source files 
|    ├── main.py     <- driver program file 
|    ├── task1.py    <- task 1 implemented here 
|    ├── ...
|    └── task4.py    <- task 4 implemented here 
│                               
├── ....             <- bla bla bla
└── Readme.md

The main.py file contains a couple of functions containing lambda expressions within, quadratic equation solver function and pascal triangle printer function for testing.
Recursive functions were avoided


## Task 1

We create a function decorator that calculates function execution time and the number of times the decorated function was called (function call trace). We make sure that the implementation works for multiple functions. Below you can see an example of the overall python program expected behavior and implementation script:

$ cat main.py
import random
from task1 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()

$ python main.py 
func call 1 executed in 0.0130 sec
funx call 1 executed in 0.4130 sec
func call 2 executed in 0.1130 sec
funx call 2 executed in 0.0031 sec
func call 3 executed in 0.0031 sec

## Task 2

We extend the implementation so that the decorator could dump original source code of the function. Each function to be decorated should have a docstring. What is a docstring?. To inspect and manipulate function objects see inspect module. Here is an example of the overall python program expected behavior and implementation script:

$ cat main.py
from task2 import decorator_2

@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    print("some\nmultiline\noutput")

if __name__ == "__main__": 
    funh(None, bar2="")

$ python main.py

funh call 1 executed in 0.0130 sec
Name:   funh
Type:   <class 'function'>
Sign:   (bar1, bar2='')
Args:   positional (None,) 
        key=worded {'bar2': ''}
        
Doc:    This function does somthing useful
        :param bar1: description
        :param bar2: description

Source: @decorator_2
        def foo(bar1, bar2=""):
        """
        This function does something useful 
        :param bar1: description
        :param bar2: description
        """ 
        print("some\nmultiline\noutput")

Output: some
        multiline
        output

## Task 3

We implement the decorator behavior in tasks 1 & 2 using a class decorator. All the program output (from the decorator) is dumped into an `output.txt` file. We rank the functions used to test the implementation based on the last execution information and plot a rankings table. i.e
Hint: use a global variable

python main.py
PROGRAM | RANK | TIME ELAPSED
fun1        1     0.011488118s
fun3        2     0.020115991s
fun2        3     0.045907541s
fun4        4     0.045907541s

## Task 4

Again, we extend the program (class decorator) so that if a decorated function encounters an error it wouldn’t put it back into stdout. Instead, we pipe the error stream into a `log.txt` file together with a timestamp. Test both the class decorator and function decorator
Hint: Use Try and Except statements


