# list comprehensions: create the whole list in memory at the start
# generators: generate on-the-fly (less memory, but can be slower)

# list comprehension:
xyz = [i for i in range(5)]

# generator
xyz = (i for i in range(5))

# in python, parens are used for prioritizing operations, creating tuples, and generator expressions


### another generator example
input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))

# list comprehensions can incorporate a function
# [print(i) for i in xyz]

# complex, nested list comprehension
[[print(i, ii) for ii in range(2)] for i in range(3)]
# identical to:
for i in range(3):
    for ii in range(2):
        print(i, ii)
