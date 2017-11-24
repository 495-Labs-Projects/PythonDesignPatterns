from fixed_meal_class import *

# This is the client code trying to interact with the the correct meal class.

# Here let's just first declare some variables for each field
customer_name = "John"
order_number = 1


# Using MealBuilder
# As mentioned before we don't need to know everything beforehand since we can just build up the
# meal using the MealBuilder step by step. Also it allows for modifications like on line 25.
# We can build the meal by stringing together a bunch of these modification method calls.
# Lastly, when the user decides that he/she has finished ordering, the a finalized Meal object
# will be created.
# If a meal is created before the Meal object is complete, then it will throw and error like
# on line 20.

meal_builder = MealBuilder(customer_name, order_number)
# meal = meal_builder.build()
meal_builder.add_drink(Drink("Coke")).add_drink(Drink("Sprite"))
meal_builder.add_food_item(FoodItem("Burger")).add_food_item(FoodItem("Pizza"))
meal_builder.add_side(Side("Fries")).add_side(Side("Mashed Potatoes"))
meal_builder.add_toy(Toy("Lego")).add_toy(Toy("Superman"))
meal_builder.add_side(Side("Mac n Cheese"))
# meal if of type Meal
meal = meal_builder.build()
print(meal.get_total())