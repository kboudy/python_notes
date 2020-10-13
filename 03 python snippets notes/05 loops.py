"""
for/else
"""
for i in range(5):
    pass
else:  # else executes after the loop, *if no break statements were hit*
    pass

i = 1
while i < 6:
    print(i)
    i += 1
else:  # as in the "for" example above, else executes after the loop, *if no break statements were hit*
    print("i is no longer less than 6")
