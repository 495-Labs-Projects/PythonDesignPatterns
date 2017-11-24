# items.py
# This file just contains some quick boiler plate concrete classes for menu items.
# These menu items will be used to build up the full meal and will be used in the meal class.
# In actualilty these should be abstract classes with actual concrete items for each type like coke or sprite rather than just drink.

class Item:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price

  @property
  def name(self):
    return self.__name

  @property
  def price(self):
    return self.__price


class Drink(Item):
  def __init__(self, name, price=2):
    super().__init__(name, price)


class FoodItem(Item):
  def __init__(self, name, price=5):
    super().__init__(name, price)


class Side(Item):
  def __init__(self, name, price=2):
    super().__init__(name, price)


class Toy(Item):
  def __init__(self, name, price=1):
    super().__init__(name, price)


class Note:
  def __init__(self, note):
    self.__note = note

  @property
  def note(self):
    return self.__note