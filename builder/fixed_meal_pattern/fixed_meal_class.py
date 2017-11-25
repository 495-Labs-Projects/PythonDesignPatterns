from items import *
from abc import abstractmethod

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


# Correct Way
# This is one way to fix all the problems that we mentioned before using the builder pattern. With this pattern
# we will need to create two separate classes, one is for the actual Meal and another called MealBuilder to
# contain the state while building up the meal. 
#
# This whole layout fixes all the problems listed before since now:
#  - We don't need to know every single value before creating a new instance of this class
#  - There's an easy way to keep track of the invariants of this class (required fields and optionals)
#  - The Meal class won't break the rule of being immutable, but the MealBuilder allows clients to make 
#    modifications before building the final Meal
#  - The Meal can't be in an inconsistent/incomplete state since the build method checks the invariants
#    and the MealBuilder will hold any temporary inconsisten/incomplete states


# The Meal class in this case will only take in a builder and build up the meal using that object.
# This class will gaurantee to be a consistent and complete state while still making sure that nothing can 
# be modified after creation. There are still getters in place for each field so that the client can view 
# the private fields after creation.

class Meal:
  def __init__(self, builder):
    self.__customer_name = builder.customer_name
    self.__order_number = builder.order_number
    self.__drinks = builder.drinks
    self.__food_items = builder.food_items
    self.__sides = builder.sides
    self.__toys = builder.toys
    self.__notes = builder.notes

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


# This is just a short interface created for builders that contain an abstract build method.
# Generally the build method is supposed to be called once the client is done building up the
# object and will return the final built object (in this case a Meal).

class BuilderInterface:
  @abstractmethod
  def build(self):
    pass


# This is a concrete implementation of the BuilderInterface that implemenets the build method.
# The MealBuilder will have a constructor containing all the required fields and sets default
# values for the other fields. 
#
# Because the builder doesn't need to follow the rules of the meal, since its only an intermediary
# state/step, we don't need to make each field private. Also we will have methods that allow the client
# to modify each field. The client will create a build and throughout the ordering process, will build
# up the meal step by step (allowing for any modifications).
#
# Lastly there is the build method which is called one the client is done building up the Meal object and
# it will return the final Meal object. In the build method it will also check the invariants needed to make
# sure that the Meal's invariants are met before returning it. 

class MealBuilder(BuilderInterface):
  def __init__(self, customer_name, order_number):
    self.customer_name = customer_name
    self.order_number = order_number
    self.drinks = []
    self.food_items = []
    self.sides = []
    self.toys = []
    self.notes = []

  def add_drink(self, drink):
    self.drinks.append(drink)
    return self

  def add_food_item(self, food_item):
    self.food_items.append(food_item)
    return self

  def add_side(self, side):
    self.sides.append(side)
    return self

  def add_toy(self, toy):
    self.toys.append(toy)
    return self

  def add_notes(self, note):
    self.notes.append(note)
    return self

  def __check_invariant(self, meal):
    if(len(meal.drinks) + len(meal.food_items) + len(meal.sides) + len(meal.toys) == 0):
        raise Exception("Need to have some items to create a meal") 

  def build(self):
    meal = Meal(self)
    # Note: we check the invariants after creating the meal in order to be thread safe, because
    # if we checked the invarants before instantiating the meal, then another thread could potentially
    # change the fields of the builder right after the check and before the instantiation.
    self.__check_invariant(meal)
    return meal

