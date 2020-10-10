items = ["left", "right", "up", "down"]

# kludgy:
for i in range(len(items)):
    print(i, items[i])

# better - use enumerate, which produces a tuple of (index, item)
for i, item in enumerate(items):
    print(i, item)

# you can also create a dictionary where the keys are the indexes:
new_dict = dict(enumerate(example))