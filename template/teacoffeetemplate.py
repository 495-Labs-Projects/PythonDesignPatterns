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

if __name__ == "__main__":
    main()
