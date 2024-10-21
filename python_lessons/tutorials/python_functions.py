"""

A function is 
   a piece of code that carry out a repeatable specified or 
   set of repeatable specified code instruction 
   1. returnable
   2. none returnable
 
 or = logical operator
 |  = declarative or 
"""

from typing import Callable


def add(a: int | float, b: int | float) -> int | float:
    return a + b


c = add(a=1, b=2)

print(c)

num_1 = 4
num_2 = 5

num_3 = add(num_1, num_2)

print(num_3)


def sayHi(name: str):
    print(f"Hi {name}")

sayHi("Adam")
sayHi("Kahse")
sayHi("Awet")
sayHi("Grande")

""" 
 arguments are divided in to two
 1. named references
 2. unnamed references
 
 1. supplied value
 2. defaulted value
"""

def greet( name: str, greeting: str = "ኣታ ከመይ ከ",):
    print(f"{name} {greeting}")
    
greet("ኣዳም",)


"""
 what is a factorial
 
 4! = 4*3*2*1
    = 24
    
first iteration
    4 * factorial(3) = 4*3---factorial(3)
second iteration
    3 * factorial(2) = 4 * 3 * 2---factorial(2)

third iteration
    2 * factorial(1) = 4 * 3 * 2 * 1---factorial(1)
    
result = 24
"""
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

four_factorial = factorial(4)
print(four_factorial)

""" 
lambda: a syntactic sugar of single line function

  parameters: operation
  lambda parameters: operation
"""


add_numbers = lambda x, y: x+y

print(add_numbers(3,5))

sqr = lambda x: x**2 # x*x

print(sqr(9))

qbr = lambda x: x**3

print(qbr(9))


def sqr_func(x: int) -> int:
    return x **2
    
numbers = [2, 8, 3, 4]

"""
  map takes two parameters 
    1. reducer/operator [ function, lambda]
    2. collection [list, dict, tuple, set]
"""
""" 
1. it constructs an empty list
2. it converts the set to a list 
numbers_ { } = [ ] and loops over it
3. in each loop  square the element and append it to
    the list sqr_numbers
    
4. convert sqr_numbers to set and return it



"""
def map_x(numbers_: list[int], z: Callable) -> list[int]:
    # construct empty list
    sqr_numbers = []  # [4, 9, 16, 64 ]
    # {2, 3, 4, 8} = [2, 3, 4, 8]
    for number in numbers_:
        sqr_number = z(number)
        sqr_numbers.append(sqr_number)
        
    #  [2, 3, 4, 8] = {2, 3, 4, 8}
    return sqr_numbers
    
sqr_numbers_1 = map_x(numbers, lambda x: x**2)
print(sqr_numbers_1)

sqr_numbers_2 = map(lambda x: x**2 , numbers)
print(list(sqr_numbers_2))


""" 
lambda x: x %2==0
"""
def func(x:int): # lambda x:
    return x % 2 == 0 # x %2==0

def filter_x(func:Callable, numbers: list[int])-> list[int]:
    even_numbered_lists = []
    
    for number in numbers:
        if func(number):
            even_numbered_lists.append(number)
            
    return even_numbered_lists

even_numbered = filter_x(func, numbers,)
print(even_numbered)

def filter_x_2(numbers: list[int])-> list[int]:
    even_numbered_lists = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbered_lists.append(number)
            
    return even_numbered_lists

even_numbered = filter_x_2(numbers)

print(even_numbered)

even_numbers = filter(lambda x: x %2==0, numbers)

print(list(even_numbers))
 
""" 
lists as function parameters = params
                  arguments = args
func = function name
(...) = function signature or function arguments of function parameters
 function signatures can be represented either by
   1. list/tuple
   2. dictionary
def func(...):
"""
kwargs = dict(name="Alice", age=25, job="Engineer") 
args = list(kwargs.values())
 
def arg_func(*argus):  
    print(argus[0])
    
name, age, job = ['Alice', 25, 'Engineer'] # *args = 'Alice', 25, 'Engineer'

arg_func(args) #(['Alice', 25, 'Engineer'])
arg_func(*args) # *args = 'Alice', 25, 'Engineer'
arg_func('Alice', 25, 'Engineer')
    
def kwargs_func(**kwargs):  
    print(kwargs["name"])
print("-=-------------------------------------=-")
kwargs_func(**kwargs) # **kwargs = name="Alice", age=25, job="Engineer"
kwargs_func(name="Alice", age=25, job="Engineer")



 
