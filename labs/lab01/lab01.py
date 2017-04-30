## Boolean Operators ##
# Alexandra Dotterweich
# SID 24091905


# Q3
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return y > 0 and x > 0

# Q4
def gets_discount(x, y):
    """ Returns True if this is a combination of a senior citizen
    and a child, False otherwise.

    >>> gets_discount(65, 12)
    True
    >>> gets_discount(9, 70)
    True
    >>> gets_discount(40, 45)
    False
    >>> gets_discount(40, 75)
    False
    >>> gets_discount(65, 13)
    False
    >>> gets_discount(7, 9)
    False
    >>> gets_discount(73, 77)
    False
    >>> gets_discount(70, 31)
    False
    >>> gets_discount(10, 25)
    False
    """
    "*** YOUR CODE HERE ***"
    return x > 64 and y <= 12 or x <= 12 and y > 64

# Q5
def is_factor(x, y):
    """ Returns True if x is a factor of y, False otherwise.

    >>> is_factor(3, 6)
    True
    >>> is_factor(4, 10)
    False
    >>> is_factor(0, 5)
    False
    >>> is_factor(0, 0)
    False
    """
    "*** YOUR CODE HERE ***"
    return x != 0 and y % x == 0 

## if statements ##

# Q8
def compare(a, b):
    """Compares if a and b are equal.

    >>> compare(4, 2)
    'not equal'
    >>> compare(4, 4)
    'equal'
    """
    if a == b:
        return 'equal'
    return 'not equal'


## while loops ##

# Q10
def factors(n):
    """
    Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    a = n 
    while a > 0 :
        if n % a == 0 :
            print (a)
        a = a - 1

