# CS 61A Summer 2014
# Name: Alexandra Dotterweich
# Login: cs61a-jd

############
# Nonlocal #
############

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    counter = [0]
    def accumulate (number):
        counter [0] += number
        return counter[0]
    return accumulate
        
   

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    counter = 0 
    def accumulate(number):
        nonlocal counter
        counter += number
        return counter
    return accumulate



#######
# OOP #
#######

class Amount(object):
    """An amount of nickels and pennies.

    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value 
    22
    >>> a.nickels = 5
    >>> a.value
    32

    """
    "*** YOUR CODE HERE ***"
    def __init__(self, nickels, pennies):
        self.nickels = nickels
        self.pennies = pennies

    @property
    def value(self):
        return (self.nickels * 5) + self.pennies


class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than
    four pennies, by converting excess pennies to nickels.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels, a.pennies, a.value  # Creates a tuple
    (4, 2, 22)
    >>> a = MinimalAmount(7, 3)
    >>> a.nickels, a.pennies, a.value
    (7, 3, 38)
    >>> a = MinimalAmount(0, 50)
    >>> a.nickels, a.pennies, a.value
    (10, 0, 50)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, nickels, pennies): #this is making all amounts minimal
        self.nickels = nickels
        self.pennies = pennies
        if pennies > 4: #as long as there is more than 4 pennies, they can be converted to nickels?
            self.nickels += pennies // 5
            self.pennies -= (pennies // 5) * 5


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(1)
    'Current candy stock: 1'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.restock(1)
    'Current candy stock: 2'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.vend()
    'Machine is out of stock.'
    >>> p = VendingMachine('pepsi', 21)
    >>> p.restock(100)
    'Current pepsi stock: 100'
    >>> p.deposit(100)
    'Current balance: $100'
    >>> p.vend()
    'Here is your pepsi and $79 change.'
    >>> p.deposit(21)
    'Current balance: $21'
    >>> p.vend()
    'Here is your pepsi.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.stock = 0
        self.balance = 0 
        self.product = product
        self.price = price

    def vend(self): #vend is called with no arguments 
        if self.stock == 0:
            return 'Machine is out of stock.'  
        elif self.balance < self.price:
            difference = self.price - self.balance
            return 'You must deposit ${0} more.'.format(difference)
        elif self.balance == self.price:
            self.stock = self.stock - 1
            self.balance = 0
            return 'Here is your {0}.'.format(self.product)
        else:
            difference = self.balance - self.price
            self.stock = self.stock - 1
            self.balance = 0
            return 'Here is your {0} and ${1} change.'.format(self.product, difference)       

    def deposit(self, amount): 
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            self.balance = self.balance + amount
            return 'Current balance: ${0}'.format(self.balance)

    def restock(self, amount): #takes in a monetary amount
        self.stock = self.stock + amount 
        return 'Current {0} stock: {1}'.format(self.product, self.stock)

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, input):
        self.input = input 

    def ask(self, string, *args):
        string_list = str.split(string)
        if string_list[0] == 'please':
            string_list = string_list[1:]
            if string_list[0] == 'vend':
                return getattr(self.input, 'vend')()
            if string_list[0] =='deposit':
                return getattr(self.input, 'deposit')(args[0])
            else:
                new = ''
                i = 0
                while len(string_list)-1 >= i:
                    new += string_list[i]
                    if i <= len(string_list[i])-1:
                        new += ' '
                    i += 1
                print(new)
                return 'Thanks for asking, but I know not how to {0}'.format(new)
        else:
            return 'You must learn to say please first.'

############
# Optional #
############

# def make_withdraw(balance, password):
#     """Return a password-protected withdraw function.

#     >>> w = make_withdraw(100, 'hax0r')
#     >>> w(25, 'hax0r')
#     75
#     >>> w(90, 'hax0r')
#     'Insufficient funds'
#     >>> w(25, 'hwat')
#     'Incorrect password'
#     >>> w(25, 'hax0r')
#     50
#     >>> w(75, 'a')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     40
#     >>> w(20, 'n00b')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
#     >>> w(10, 'l33t')
#     "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
#     """
#     "*** YOUR CODE HERE ***"

# # Old version
# def count_change(a, coins=(50, 25, 10, 5, 1)):
#     if a == 0:
#         return 1
#     elif a < 0 or len(coins) == 0:
#         return 0
#     return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# # Version 2.0
# def make_count_change():
#     """Return a function to efficiently count the number of ways to make
#     change.

#     >>> cc = make_count_change()
#     >>> cc(500, (50, 25, 10, 5, 1))
#     59576
#     """
#     "*** YOUR CODE HERE ***"





