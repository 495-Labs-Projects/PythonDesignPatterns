from wrong_meal_class import *
from fixed_meal_class import *

customer_name = "John"
order_number = 1
drinks = [Drink("Coke"), Drink("Sprite")]
food_items = [FoodItem("Burger"), FoodItem("Pizza")]
sides = [Side("Fries"), Side("Mashed Potatoes"), Side("Mac n Cheese")]
toys = [Toy("Lego"), Toy("Superman")]
notes = [Note("No pickles")]

wrong_meal1 = WrongMeal1(customer_name, order_number, drinks, food_items, sides, toys, notes)
# print(wrong_meal1.__customer_name)
print(wrong_meal1.get_total())

wrong_meal2 = WrongMeal2()
wrong_meal2.customer_name = customer_name
wrong_meal2.order_number = order_number
wrong_meal2.drinks = drinks
wrong_meal2.food_items = food_items
wrong_meal2.sides = sides
wrong_meal2.toys = toys
wrong_meal2.notes = notes
print(wrong_meal2.get_total())


meal_builder = MealBuilder(customer_name, order_number)
# meal = meal_builder.build()
meal_builder.add_drink(Drink("Coke")).add_drink(Drink("Sprite"))
meal_builder.add_food_item(FoodItem("Burger")).add_food_item(FoodItem("Pizza"))
meal_builder.add_side(Side("Fries")).add_side(Side("Mashed Potatoes"))
meal_builder.add_toy(Toy("Lego")).add_toy(Toy("Superman"))
meal_builder.add_side(Side("Mac n Cheese"))
meal = meal_builder.build()
print(meal.get_total())