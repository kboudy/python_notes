x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = ["a", "b", "c", "d"]

for a, b, c in zip(x, y, z):
    print(a, b, c)
"""
1 5 a
2 6 b
3 7 c
4 8 d
"""

# zip produces a "zip object" - you need to convert it to a list
print(list(zip(x, y, z)))
# [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c'), (4, 8, 'd')]

# using list comprehension
[print(a, b, c) for a, b, c in zip(x, y, z)]
