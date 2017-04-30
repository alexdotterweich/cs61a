# CS 61A Spring 2014
# Name: Alexandra Dotterweich
# Login: cs61a-jd

def square(x):
    """Return x squared."""
    return x * x

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    total, k = 1, 1
    while k <= n:
        total, k = total * term(k), k + 1
    return total 

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    "*** YOUR CODE HERE ***"
    if n < 1: 
        return 1 
    else: 
        return n * factorial(n-1) 

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    "*** YOUR CODE HERE ***"
    total, k = start, 1 
    while k <= n: 
        total, k = combiner(total, term(k)), k + 1
    return total 

    

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    "*** YOUR CODE HERE ***"
    return accumulate((lambda x, y: x + y), 0, n, term) 

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    return accumulate((lambda x, y: x * y), 1, n, term)
   
def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    "*** YOUR CODE HERE ***"
    def helper_funct(x): 
        counter = 0
        while counter < n :
            x, counter = f(x), counter + 1 
        return x
    return helper_funct


def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))


def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))




