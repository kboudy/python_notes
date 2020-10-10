#######
# map #
#######

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)


# In Python 2.x, map() returns a list. This behavior changed in Python 3.x
# Now, map() returns a map object, which is an iterator that yields items on demand
# That’s why you need to call list() to create the desired list object.
print(list(squared)) # [1, 4, 9, 16, 25]


##########
# filter #
##########

numbers = [0, 1, 2, 3, 5, 8, 13] 

even_numbers = filter(lambda x: x % 2 == 0, numbers) 
print(list(even_numbers)) # [0, 2, 8]


##########
# reduce #
##########

from functools import reduce

# simple adder
numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers))

# with an initializer (0)
def sum_even(it):
     return reduce(lambda x, y: x + y if not y % 2 else x, it, 0)
print(sum_even([1, 2, 3, 4])) # 6
