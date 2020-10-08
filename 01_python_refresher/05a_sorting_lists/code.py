# Sorting a simple list by a custom function
carNames = ['Ford','Mitsubishi','BMW','VW']
carNames.sort(key=lambda c:len(c))
print(carNames)

# Sorting a list of dictionary items by one of the keys
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=lambda c:c["year"])
print(cars)
