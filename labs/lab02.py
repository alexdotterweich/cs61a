# Q3

def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***" 
    return (lambda: 3)()

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    #f2()() == blah()
    return (lambda: lambda: 3)()

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return (lambda: lambda x: x)()

def f4():
    """
    >>> f4()()()
    3
    """
    "*** YOUR CODE HERE ***"
    return (lambda: lambda: lambda: 3)()

def f5():
    """
    >>> f5()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return (lambda: lambda: lambda x:  lambda: 3)()

# Q5

def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.
    
    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    def helper_funct(x):
        number = 0
        while x > number :
            if number % n == 0:
                print('Buzz!')
            else :
                print(number)
            number += 1
    return helper_funct

#When testing this, expected and got are the same, however the test says that they're not 


# Q6

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def function_call_helper(n) : #takes in n 
        def cycle_helper (x) : #applies functions 
            counter = 0 
            while counter < n : 
                if  counter % 3 == 0 : #1st function 
                    x = f1(x)
                elif counter % 3 == 1 : #2nd 
                    x = f2(x) 
                else :
                    x = f3(x) 
                counter += 1 
            return x
        return cycle_helper 
    return function_call_helper


# Functional representation of pairs

def cons(a, b):
    def answer(m):
        if m == 'car':
            return a
        else:
            return b
    return answer

def car(p):
    return p('car')

def cdr(p):
    return p('cdr')


# Implementation of linked lists using cons

empty = lambda: 42

def link(element, list):
    return cons(element, list)

def first(list):
    return car(list)

def rest(list):
    return cdr(list)

def print_linked_list(list):
    s = '<'
    while list != empty:
        s = s + (first(list)) + ' '
        list = rest(list)
    return s[:-1] + '>'
        

# Q7

def sum_linked_list(lst, term):
    """ Applies a function TERM to each number in LST and returns the sum
    of the resulting values

    >>> square = lambda x: x*x
    >>> double = lambda y: 2*y
    >>> lst1 = link(1, link(2, link(3, link(4, empty))))    
    >>> sum_linked_list(lst1, square)
    30
    >>> lst2 = link(3, link(5, link(4, link(10, empty))))
    >>> sum_linked_list(lst2, double)
    44
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return 0
    else: 
        return term(first(lst)) + sum_linked_list(rest(lst), term)


