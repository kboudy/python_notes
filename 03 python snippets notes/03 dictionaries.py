car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)  # {}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.copy()
print(x)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

x = ("key1", "key2", "key3")
thisdict = dict.fromkeys(x)
print(thisdict)  # {'key1': None, 'key2': None, 'key3': None}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("price", 15000)
print(car)  # 15000 (default, since the property doesn't exist)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()
# note that items() continues to update after it's been called:
car["year"] = 2018
print(x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
car["color"] = "white"
print(x)  # dict_keys(['brand', 'model', 'year', 'color'])

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)  # {'brand': 'Ford', 'year': 1964}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()
print(car)  # {'brand': 'Ford', 'model': 'Mustang'}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("color", "white")  # only sets the key/value if it doens't exist
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
print(x)  # white

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
# note that values() continues to update after it's been called:
car["year"] = 2018
print(x)  # dict_values(['Ford', 'Mustang', 2018])
