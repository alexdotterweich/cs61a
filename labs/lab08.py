# Q2
class Person(object):
    """
    Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat()       # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """

    def __init__(self, name):
        self.name = name
        self.thing_said = 'I squirreled it away before it could catch on fire.'

    def say(self, stuff):
        self.thing_said = stuff
        return stuff

    def ask(self, stuff):
        self.thing_said = self.say("Would you please " + stuff)
        return self.say("Would you please " + stuff)

    def greet(self):
        self.thing_said = self.say("Hello, my name is " + self.name)
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.thing_said

# Q3
class DoubleTalker1(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff) + " " + self.repeat()

class DoubleTalker2(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return stuff + " " + stuff

class DoubleTalker3(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff + " " + stuff)

# Choose the REAL DoubleTalker
DoubleTalker = DoubleTalker3 # Either DoubleTalker1, DoubleTalker2, or DoubleTalker3

def test_doubletalker():
    """ I exist only to test that you've made the right choice.

    >>> steven = DoubleTalker("Steven")
    >>> steven.say("hello")
    'hello hello'
    >>> steven.say("the sky is falling")
    'the sky is falling the sky is falling'
    >>> steven.repeat()
    'the sky is falling the sky is falling'
    """
    pass


# # Q4
class Account(object):
    """
    A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance."""
        self.balance = self.balance + amount
        self.transactions += [('deposit', self.balance)]
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions += [('withdraw', amount)]
        return self.balance

# # Q5
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check('Steven', 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount('Steven')
    >>> eric_account = CheckingAccount('Eric')
    >>> eric_account.deposit_check(check)  # trying to steal steven’s money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    
    """
    withdraw_fee = 1
    interest = 0.01

    def deposit_check(self, check):
        if check.person == self.holder:
            if check.deposited: 
                print('The police have been notified.')
            else:
                check.deposited = True
                return self.deposit(check.amount)
        if check.person != self.holder:
            print('The police have been notified.')

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


# Don't forget to modify CheckingAccount above!

class Check(object):
    "*** YOUR CODE HERE ***"
    def __init__(self, person, amount):
        self.person = person
        self.amount = amount
        self.deposited = False 

# # Q6
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and
    has a dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        "*** YOUR CODE HERE ***"
        self.buttons = []
        for i in args:
            self.buttons.append(i)
            

    def press(self, info):
        """Takes in a position of the button pressed, and 
        returns that button's output"""
        "*** YOUR CODE HERE ***"
        for button in self.buttons:
            if info == button.pos:
                button.pressed += 1
                return button.key

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and 
        returns the total output"""
        "*** YOUR CODE HERE ***"
        total = ''
        for i in typing_input:
            total += self.press(i)
        return total 

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0

def button_press(positions, keyboard):
    """Takes in a list of positions, and returns what
    keyboard would print

    >>> b1 = Button(8, "B")
    >>> b2 = Button(5, "A")
    >>> b3 = Button(1, "N")
    >>> kboard = Keyboard(b1, b2, b3)
    >>> button_press([8, 5, 1, 5, 1, 5], kboard)
    'BANANA'
    """
    "*** YOUR CODE HERE ***"
    word = ''
    for letter in positions:
        word += keyboard.press(letter)
    return word 


