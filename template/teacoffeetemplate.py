"Add in hooks as well"


class TeaClass1():

    def prepareRecipe(self):
        self.boilWater()
        self.steepTeaBag()
        self.pourInCup()
        self.addLemon()

    def steepTeaBag(self):
        print("Steeping the tea")

    def addLemon(self):
        print("Adding lemon")

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

class CoffeeClass1():

    def prepareRecipe(self):
        self.boilWater()
        self.brewCoffeeGrinds()
        self.pourInCup()
        self.addSugarAndMilk()

    def brewCoffeeGrinds(self):
        print("Dripping coffee through filter")

    def addSugarAndMilk(self):
        print("Adding sugar and milk")

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

 
"""
PROBLEM: We have two classes with similar functionality. We are writing more code than we need to because some of the functionality overlaps. In this case, tea and coffee have a lot of similarities and we should be able to combine them in some way to avoid redundancy in our code.


PATTERN: The template pattern defines the skeleton of an algorithm in an abstract class. Some tasks are delegated or overwritten by subclasses to remove excess code, but maintain the algorithm's structure. 

Let's make coffee and tea subclasses and create an abstract class for all of our hot beverages with the template pattern!
"""

class HotBeverageClass():

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()

    # We can delegate these steps for the respective subclasses to define
    def brew(self):
        pass

    def addCondiments(self):
        pass

    # These steps are the same for all hot beverages
    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")


class TeaClass2(HotBeverageClass):

    #The tea class overwrites the original methods to meet its criteria

    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding lemon")


class CoffeeClass2(HotBeverageClass):

    def brew(self):
        print("Dripping coffee through filter")

    def addCondiments(self):
        print("Adding sugar and milk")


"""
That's all well and good, but what if a customer doesn't want condiments? We can assume by default that the customer wants condiments, but we should at least allow them to opt out. However, the hot beverage class is the abstract class and doesn't deal directly with our customers. Instead, we'll need to allow our subclasses, coffee and tea, to determine this themselves.

We'll do this by adding in a hook method. A hook is defined in our abstract class, but given an empty or default implementation for the subclass to "hook into" the algorithm at various points. 

In this case, we write a default method in our hot beverage class and the coffee and tea subclasses overwride the default method to talk to the customer.

"""

class HotBeverageClass():

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    # Our new method, allows the subclass to "hook" in and evaluate a certain part of the algorithm
    def customerWantsCondiments(self):
        return True

    # We can delegate these steps for the respective subclasses to define
    def brew(self):
        pass

    def addCondiments(self):
        pass

    # These steps are the same for all hot beverages
    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")


class TeaClass3(HotBeverageClass):

    # Here we'll take customer input to determine whether they want lemon in their tea
    def customerWantsCondiments(self):
        response = input("Would you like lemon with your tea (y/n)? ")
        if response.lower() == "y":
            return True
        return False

    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding lemon")


class CoffeeClass3(HotBeverageClass):

    def customerWantsCondiments(self):
        response = input("Would you like milk and sugar with your coffee (y/n)? ")
        if response.lower() == "y":
            return True
        return False

    def brew(self):
        print("Dripping coffee through filter")

    def addCondiments(self):
        print("Adding sugar and milk")

def main():
    t1 = TeaClass1()
    c1 = CoffeeClass1()
    t1.prepareRecipe()
    print("\n")
    c1.prepareRecipe()
    print("\n")
    tea_class = TeaClass2()
    tea_class.prepareRecipe()
    print("\n")
    coffee_class = CoffeeClass2()
    coffee_class.prepareRecipe()
    print("\n")
    t3 = TeaClass3()
    c3 = CoffeeClass3()
    t3.prepareRecipe()
    print("\n")
    c3.prepareRecipe()
    print("\n")

if __name__ == "__main__":
    main()
    

