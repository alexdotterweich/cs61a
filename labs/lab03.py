# Q1

def sum_every_number(n):
    """Return the sum of every natural number up to n, inclusive.
    
    >>> sum_every_number(5)
    15
    """
    if n == 1:
        return 1
    else:
        return n + sum_every_number(n - 1)


def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.
    
    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 1: 
        return 1 
    elif n == 0:
        return 0
    else:
        return n + sum_every_other_number(n - 2)
            


def fibonacci(n):
    """Return the nth fibonacci number.
    
    >>> fibonacci(11)
    89
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_up_to(n):
    """Print every natural number up to n, inclusive.
    
    >>> print_up_to(5)
    1
    2
    3
    4
    5
    """
    i = 1
    if i > n:
        return 1  
    else:
        i += 1 
        print_up_to(n-1)
        print(n)


# Q2

# Functional representation of pairs

# Don't worry if you don't understand this yet.
class PairError(Exception):
    pass

def cons(a, b):
    def answer(m):
        if m == 'car':
            return a
        elif m == 'cdr':
            return b
        else:
            # This is a way for us to create our own error messages.
            raise PairError('You can only use car or cdr on a pair!')
    return answer

def car(p):
    return p('car')

def cdr(p):
    return p('cdr')


# Implementation of linked lists using cons

empty = lambda: 42

def link(element, lst):
    return cons(element, lst)

def first(lst):
    return car(lst)

def rest(lst):
    return cdr(lst)

def print_linked_list(lst):
    print(linked_list_to_str(lst))

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s[:-1] + ' >'
        

def map(f, lst):
    """Returns a list of the results produced by applying f to each
    element in lst.

    >>> my_list = link(1, link(2, link(3, link(4, empty))))
    >>> print_linked_list(map(lambda x: x * x, my_list))
    < 1 4 9 16 >
    >>> pokemon = link('bulbasaur', link('charmander', link('squirtle', empty)))
    >>> print_linked_list(map(print, pokemon))
    bulbasaur
    charmander
    squirtle
    < None None None >
    """
    "*** YOUR CODE HERE ***"
    if lst == empty :
        return empty
    else : 
        return link(f(first(lst)), map(f, rest(lst)))
# Q3

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b <= a :
        if a % b == 0 :
            return b 
        else :
            return gcd(b, a % b) 

    elif b >= a :
        if b % a == 0 :
            return a
        else :
            return gcd(a, b % a)


# Q4

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0: 
        print(int(n))
        return(1 + (hailstone(n/2)))
    else: 
        print(int(n))
        return(1 + (hailstone((3*n) + 1)))
    



# Q5

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1 :
        return 1 
    else : 
        return paths(m-1, n) + paths(m, n-1)


