# List Mutation
def reverse(lst):
    """Reverses lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)//2):
        counter = lst[i]
        lst[i] = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = counter


def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        lst[i] = fn(lst[i])



# # filter is optional -- finish other non-optional problems first
# def filter(pred, lst):
#     """Filters lst with pred using mutation.
#     >>> original_list = [5, -1, 2, 0]
#     >>> filter(lambda x: x % 2 == 0, original_list)
#     >>> original_list
#     [2, 0]
#     >>> original_list2 = ['cool', 'nice', 'rad']
#     >>> filter(lambda x: len(x) == 4, original_list2)
#     >>> original_list2
#     ['cool', 'nice']
#     """
#     "*** YOUR CODE HERE ***"


# Dictionaries
def counter(message):
    """ Returns a dictionary of each word in message mapped 
    to the number of times it appears in the input string.
    >>> x = counter("to be or not to be")
    >>> x["to"]
    2
    >>> x["be"]
    2
    >>> x["not"]
    1
    >>> y = counter("run forrest run")
    >>> y["run"]
    2
    >>> y["forrest"]
    1
    """
    word_list = message.split()
    "*** YOUR CODE HERE ***"
    new_dict = {}
    for word in word_list:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict

# Adding in Nonlocal

cs61a = {
    "Homework": 2,
    "Lab": 1,
    "Exam": 50,
    "Final": 80,
    "PJ1": 20,
    "PJ2": 15,
    "PJ3": 25,
    "PJ4": 30,
    "Extra credit": 0
    }

def make_glookup(class_assignments):
    """ Returns a function which calculates and returns
    the current grade out of what assignments have
    been entered so far.
    
    >>> student1 = make_glookup(cs61a) #cs61a is the above dictionary
    >>> student1("Homework", 1.5)
    0.75
    >>> student1("Lab", 1)
    0.8333333333333334
    >>> student1("PJ1", 18)
    0.8913043478260869
    >>> student2 = make_glookup(cs61a)
    >>> student2("Homework", 2)
    1.0
    """
    count = 0 
    total = 0
    def helper(key, value):
        nonlocal count, total
        count += value
        total += class_assignments[key]
        return count/total
    return helper
 



