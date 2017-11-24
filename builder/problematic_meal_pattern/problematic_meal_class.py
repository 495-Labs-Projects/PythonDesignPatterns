from items import *

# Scenario
# We trying to build up a system that will map out the ordering process for customers.
# This will include the meal ordering process and some sort of class that will represent each 
# customer's meal. Each of these meals will include different menu items of each category which
# is represented in the items.py file. 
#
# Some things that we should keep in mind for this scenario is that a customer_name and order_number
# is required, while everything else is not. However, a meal has to contain at least one item, so
# drinks, food_items, sides, or toys have to be non-emtpy. Also once a meal is completed, we don't 
# want any more modifications on it, since the chef might have started making it already (aka immutable obj).



# This file contains 2 different wrong ways that are commonly implemeneted for this scenario.

# Wrong Way #1
#
# In this class we will need to have all the fields as private, since we don't want any clients modifying
# the values of them without proper permission. We also have a constructor with all possible fields and 
# a getter for each of the fields as well.
#
# Problem
# Since we are trying create this class ProblematicMeal1 to represent a meal, there are 2 main problems
# with this representation:
#  - We have to know every single value before creating a new instance of this class
#  - There's no easy way to keep track of the invariants of this class (required fields and optionals)

# Note: We can try to solve the first problem by putting in defaults for all the optional fields, 
# but then we can't really check for the invariants. We still have the problem of having to know
# all the final values of each field, since there's no way to modify the fields after initializing it.
# Also the default values way is pretty Python specific, in other languages it can be hard even to do this way.

class ProblematicMeal1:
  # def __init__(self, customer_name, order_number, drinks=[], food_items=[], sides=[], toys=[], notes=[]):
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


# Wrong Way #2
#
# In this class we will need to have all the fields as private, since we don't want any clients modifying
# the values of them without proper permission. We also have a constructor with no parameters and just 
# getters and setters for the client to later on build up the object. 
#
# Problem
# This does solve the issue of not needing to know everything when creating the object. However another
# problem comes up with this design:
#  - There's no easy way to keep track of the invariants of this class (required fields and optionals)
#  - This breaks the rule that a meal can't be changed after creation since there are setters
#  - Also similar to the first problem, the meal could be in an inconsistent/incomplete state.

class ProblematicMeal2:
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
