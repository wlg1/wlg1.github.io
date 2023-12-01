# __getitem__

This treats the object like a dictionary by specifying in `__getitem__` which dict attribute to use as the dictionary.

[NOTE: This is not the same as __getattr__, which is a getter method](https://realpython.com/python-getter-setter/)

[https://stackoverflow.com/questions/43627405/understanding-getitem-method-in-python](https://stackoverflow.com/questions/43627405/understanding-getitem-method-in-python)

Imagine a class which models a building. Within the data for the building it includes a number of attributes, including descriptions of the companies that occupy each floor :

Without using `__getitem__` we would have a class like this :

```python
class Building(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def occupy(self, floor_number, data):
          self._floors[floor_number] = data
     def get_floor_data(self, floor_number):
          return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1.occupy(0, 'Reception')
building1.occupy(1, 'ABC Corp')
building1.occupy(2, 'DEF Inc')
print( building1.get_floor_data(2) )

```

We could however use `__getitem__` (and its counterpart `__setitem__`) to make the usage of the Building class 'nicer'.

```python
class Building(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def __setitem__(self, floor_number, data):
          self._floors[floor_number] = data
     def __getitem__(self, floor_number):
          return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print( building1[2] )

```

Whether you use `__setitem__` like this really depends on how you plan to abstract your data - in this case we have decided to treat a building as a container of floors (and you could also implement an iterator for the Building, and maybe even the ability to slice - i.e. get more than one floor's data at a time - it depends on what you need.