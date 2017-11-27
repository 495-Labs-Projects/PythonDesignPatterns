class ChocolateBoiler1():

    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False
            # fill the boiler with a milk/chocolate mixture
        else:
            print("The boiler is already full.")

    def drain(self):
        if not self.empty and self.boiled:
            # drain the boiled milk and chocolate
            self.empty = True
        else:
            print("The boiler is empty or the chocolate has not been boiled.")

    def boil(self):
        if not self.empty and not self.boiled:
            #bring the contents to a boil
            self.boiled = True
        else:
            print("The boiler is empty or the chocolate has already been boiled.")

"""
PROBLEM: We have a chocolate factory with one chocolate boiler. There are a bunch of rules for the boiler as demonstrated above, but there would be a problem if we created more than one instance of the boiler class when we had only one boiler. For example, we could call fill on a boiler that's already filled. To solve this problem, we need to make sure only one instance of the chocolate boiler can be created.

PATTERN: The singleton pattern ensures a class has only one instance and provides a global point of access to it.

Let's make sure that there is only one chocolate boiler by using the singleton pattern!

"""

class ChocolateBoiler2():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ChocolateBoiler2, cls).__new__(
                                cls, *args, **kwargs)
            cls.empty = True
            cls.boiled = False
        return cls._instance


    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False
            # fill the boiler with a milk/chocolate mixture
        else:
            print("The boiler is already full.")

    def drain(self):
        if not self.empty and self.boiled:
            # drain the boiled milk and chocolate
            self.empty = True
        else:
            print("The boiler is empty or the chocolate has not been boiled.")

    def boil(self):
        if not self.empty and not self.boiled:
            #bring the contents to a boil
            self.boiled = True
        else:
            print("The boiler is empty or the chocolate has already been boiled.")


def main():
    print("Demo of the dangerous code...")
    c1 = ChocolateBoiler1()
    c2 = ChocolateBoiler2()
    c1.fill()
    c2.fill()
    assert not c1 is c2
    print("\n")
    print("Demo of the singleton pattern...")
    m1 = ChocolateBoiler2()
    print(m1.empty)
    m2 = ChocolateBoiler2()
    m2.fill()
    print(m1.empty)
    m1.drain()
    assert m1 is m2
    print("\n")

"""
The singleton pattern seems like it can be really useful, but in reality the pattern is often abused. Right now it makes sense for the chocolate factory, but if they need to add another boiler we will need to have more than one class and the singleton pattern will take a lot of work to restructure. It may not seem like an issue in this example because our current example is rather trivial and Python simplifies the pattern, however in practice if you implement a singleton pattern and need to change it later there is a lot of rewriting. It's often better to save yourself the hassle and avoid the pattern from the start.

On the other hand, one really good use for the singleton pattern is for logging to debug your code. Print statements can be a pain to comment out or delete each time we transition from debug to production. And if we move back to production we often need to add the same print statements back in again. Instead, we can write a logging class with a variable that determines whether we are in production mode or debug mode. In debug mode we log our errors to the console, however in production mode when our code is run we ignore these log statements. This way we can keep important print statements in our code and toggle one variable instead of toggling all of the print statements. Checkout the example below:

"""

class Logger():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(
                                cls, *args, **kwargs)
            cls.debug = True
        return cls._instance

    def logPrint(self, message):
        if self.debug:
            print(message)

    def inProductionMode(self):
        self.debug = False

    def inDebugMode(self):
        self.debug = True

def main2():
    print("Logging demo...")
    l = Logger()
    l.logPrint("hello world")
    l.inProductionMode()
    l.logPrint("once upon a time")
    l.inDebugMode()
    l.logPrint("once upon a time")

if __name__ == "__main__":
    main()
    main2()