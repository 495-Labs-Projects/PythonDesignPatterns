from problematic_meal_class import *

# This is the client code trying to interact with the the problematic meal class.

# Here let's just first declare some variables for each field
customer_name = "John"
order_number = 1
drinks = [Drink("Coke"), Drink("Sprite")]
food_items = [FoodItem("Burger"), FoodItem("Pizza")]
sides = [Side("Fries"), Side("Mashed Potatoes"), Side("Mac n Cheese")]
toys = [Toy("Lego"), Toy("Superman")]
notes = [Note("No pickles")]

# Using ProblematicMeal1
# As mentioned before we will have to know everything before we actually create the meal.
# If a customer tries to change their mind during the ordering process, we will have to 
# write additional code above to hold those changes before finalizing them in this instantiation.

problematic_meal1 = ProblematicMeal1(customer_name, order_number, drinks, food_items, sides, toys, notes)
print(problematic_meal1.get_total())


# Using ProblematicMeal2
# In this case we will have an incomplete state between lines 29 and 30. Also it's even harder to keep
# track and make sure that all invariants are being followed. It also breaks the rule that we can't make 
# any changes after creation since we are able to append more food_items (makes it an inconsistent state).

problematic_meal2 = ProblematicMeal2()
problematic_meal2.customer_name = customer_name
problematic_meal2.order_number = order_number
problematic_meal2.drinks = drinks
problematic_meal2.food_items = food_items
problematic_meal2.sides = sides
problematic_meal2.toys = toys
problematic_meal2.notes = notes
problematic_meal2.food_items.append(FoodItem("Pasta"))
print(problematic_meal2.get_total())
