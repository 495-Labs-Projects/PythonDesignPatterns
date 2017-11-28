"""
This is the Pizza Store example without using Abstract Factory. There
is an issue here with code that is not closed for modification.

As we can see, each implementation of the pizza store needs to implement
its own version of every type of pizza. This means that every time a
new type is added (such as veggie pizza), every pizza store location
will have to implement it as well, having to add a new "if" statement.

This can be fixed by using abstract factory to encapsulate different
types of pizza so that each location doesn't need to know about these
but rather just call the appropriate method.
"""


"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc


class PizzaStore(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def create_pizza(self, ptype):
        pass


class NYStylePizzaStore(PizzaStore):
    """
    Implement the operations to create concrete product objects.
    """

    def create_pizza(self, ptype):
        if ptype == "cheese":
            return NYStyleCheesePizza()
        else:
            return NYStyleMeatPizza()


class ChicagoStylePizzaStore(PizzaStore):
    """
    Implement the operations to create concrete product objects.
    """

    def create_pizza(self, ptype):
        if ptype == "cheese":
            return ChicagoStyleCheesePizza()
        else:
            return ChicagoStyleMeatPizza()


class NYStyleCheesePizza():
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the CheesePizza interface.
    """

    def interface_a(self):
        print("NY Style Cheese Pizza")


class ChicagoStyleCheesePizza():
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the CheesePizza interface.
    """

    def interface_a(self):
        print("Chicago Style Cheese Pizza")


class NYStyleMeatPizza():
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the MeatPizza interface.
    """

    def interface_b(self):
        print("NY Style Meat Pizza")


class ChicagoStyleMeatPizza():
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the MeatPizza interface.
    """

    def interface_b(self):
        print("Chicago Style Meat Pizza")


def main():
    for factory in (NYStylePizzaStore(), ChicagoStylePizzaStore()):
        product_a = factory.create_pizza("cheese")
        product_b = factory.create_pizza("meat")
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()