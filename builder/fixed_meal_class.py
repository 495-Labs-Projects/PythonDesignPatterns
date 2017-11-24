from items import *

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

class MealBuilder:
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
    self.__check_invariant(meal)
    return meal

