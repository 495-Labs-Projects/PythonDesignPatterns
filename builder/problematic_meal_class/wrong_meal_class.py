from items import *

class WrongMeal1:
  def __init__(self, customer_name, order_number, drinks, food_items, sides, toys, notes):
    self.__customer_name = customer_name
    self.__order_number = order_number
    self.__drinks = drinks
    self.__food_items = food_items
    self.__sides = sides
    self.__toys = toys
    self.__notes = notes

  @property
  def customer_name(self):
    return self.__customer_name

  @property
  def order_number(self):
    return self.__order_number

  @property
  def drinks(self):
    return self.__drinks

  @property
  def food_items(self):
    return self.__food_items

  @property
  def sides(self):
    return self.__sides

  @property
  def toys(self):
    return self.__toys

  @property
  def notes(self):
    return self.__notes

  def get_total(self):
    drinks_price = sum(d.price for d in self.__drinks)
    food_price = sum(f.price for f in self.__food_items)
    sides_price = sum(s.price for s in self.__sides)
    toys_price = sum(t.price for t in self.__toys)
    return drinks_price + food_price + sides_price + toys_price


class WrongMeal2:
  def __init__(self):
    pass
  @property
  def customer_name(self):
    return self.__customer_name

  @customer_name.setter
  def customer_name(self, customer_name):
    self.__customer_name = customer_name

  @property
  def order_number(self):
    return self.__order_number

  @order_number.setter
  def order_number(self, order_number):
    self.__order_number = order_number

  @property
  def drinks(self):
    return self.__drinks

  @drinks.setter
  def drinks(self, drinks):
    self.__drinks = drinks

  @property
  def food_items(self):
    return self.__food_items

  @food_items.setter
  def food_items(self, food_items):
    self.__food_items = food_items

  @property
  def sides(self):
    return self.__sides

  @sides.setter
  def sides(self, sides):
    self.__sides = sides

  @property
  def toys(self):
    return self.__toys

  @toys.setter
  def toys(self, toys):
    self.__toys = toys

  @property
  def notes(self):
    return self.__notes

  @notes.setter
  def notes(self, notes):
    self.__notes = notes

  def get_total(self):
    drinks_price = sum(d.price for d in self.__drinks)
    food_price = sum(f.price for f in self.__food_items)
    sides_price = sum(s.price for s in self.__sides)
    toys_price = sum(t.price for t in self.__toys)
    return drinks_price + food_price + sides_price + toys_price
