# CS 61A Summer 2014
# Name: Alexandra Dotterweich   
# Login: cs61a-jd

# Part I: Shakespeare and Dictionaries

def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> expected = {'and': ['to'], 'We': ['came'], 'bad': ['guys'], 'pie': ['.'], ',': ['catch'], '.': ['We'], 'to': ['investigate', 'eat'], 'investigate': [','], 'catch': ['bad'], 'guys': ['and'], 'eat': ['pie'], 'came': ['to']}
    >>> expected == table
    True
    """

    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            table[prev] += [word] 
        else:  
            key = prev  
            table[prev] = [word]
        prev = word
    return table


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    result += word + ' '
    while word not in ['.', '!', '?']:
        key = random.choice(table[word]) 
        result += key + ' '
        word = key 
    return result + word

def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)


# Part II: One-time Pass

import string, random

letter_dict ={'a':0, 'b':1, 'c':2,'d':3, 'e':4, 'f':5, 'g':6, 'h':7,
'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15,
'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
'y':24, 'z':25}

def pad_creator(word):
    """Returns a randomly-generated pad for word """
    pad = ''
    for i in range(len(word)):
        pad += random.choice(string.ascii_lowercase)
    return pad

def word_mutator(word, pad):
    """Returns an encrypted version of word using
    the one-time pass techinique.

    >>> word_mutator('charms', 'secret')
    'ulciql'
    """
    new_word = ''
    "*** YOUR CODE HERE ***"

def make_lock(pad, password, n=3):
    """Returns a function which takes in password attempts.
    If more than n passwords are attempted, then the pad is 
    locked away forever.

    If the same password is attempted more than one, the pad 
    is locked away forever.

    If the password is correct, the pad is returned, and can 
    never be retrieved again from this lock.

    >>> lock1 = make_lock('correcthorsebatterystaple', 'letmein')
    >>> lock1('bad password')
    'Sorry, wrong password. Try again?'
    >>> lock1('123456')
    'Sorry, wrong password. Try again?'
    >>> lock1('letmein')
    'correcthorsebatterystaple'
    >>> lock1('letmein')
    'Out of password attempts!'
    >>> lock2 = make_lock('xyzzy', 'worst. password. ever.')
    >>> lock2('Pikachu')
    'Sorry, wrong password. Try again?'
    >>> lock2('Pikachu')
    'Password attempt repeated: security system locked!'
    """
    attempts = []
    def lock(attempt):
        "*** YOUR CODE HERE ***"
    return lock


def OTP_encrypter(message, password):
    """Encrypts the words in the orignial list message, and
    returns a lock for the pad generated using password.
    """
    pad = []
    "*** YOUR CODE HERE ***"


