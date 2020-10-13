fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # {'orange', 'cherry', 'banana', 'apple'}

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # set()

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)  # {'cherry', 'banana', 'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)  # {'cherry', 'banana'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)  # {'google', 'microsoft'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)  # {'cherry', 'banana'}

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # {'cherry', 'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # {'apple'}

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)  # {'c'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# intersection_update removes the items in this set that are not present in other, specified set(s)
x.intersection_update(y)
print(x)  # {'apple'}

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)  # {'c'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# isdisjoint returns whether two sets have a intersection or not
result = x.isdisjoint(y)
print(result)  # False

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
result = x.issubset(y)
print(result)  # False

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
result = x.issubset(y)
print(result)  # True

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
result = x.issuperset(y)
print(result)  # True

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
result = x.issuperset(y)
print(result)  # False

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)  # {'banana', 'apple'}

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {'cherry', 'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# symmetric_difference returns the items that aren't in both sets
z = x.symmetric_difference(y)
print(z)  # {'google', 'cherry', 'microsoft', 'banana'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # {'google', 'cherry', 'microsoft', 'banana'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)  # {'google', 'apple', 'cherry', 'microsoft', 'banana'}

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)  # {'a', 'e', 'c', 'd', 'f', 'b'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# think of "update" as "union_update"
x.update(y)
print(x)  # {'google', 'apple', 'cherry', 'microsoft', 'banana'}
