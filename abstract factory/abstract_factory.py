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
    def create_cheese_pizza(self):
        pass

    @abc.abstractmethod
    def create_meat_pizza(self):
        pass


class NYStylePizzaStore(PizzaStore):
    """
    Implement the operations to create concrete product objects.
    """

    def create_cheese_pizza(self):
        return NYStyleCheesePizza()

    def create_meat_pizza(self):
        return NYStyleMeatPizza()


class ChicagoStylePizzaStore(PizzaStore):
    """
    Implement the operations to create concrete product objects.
    """

    def create_cheese_pizza(self):
        return ChicagoStyleCheesePizza()

    def create_meat_pizza(self):
        return ChicagoStyleMeatPizza()


class CheesePizza(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class NYStyleCheesePizza(CheesePizza):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the CheesePizza interface.
    """

    def interface_a(self):
        print("NY Style Cheese Pizza")


class ChicagoStyleCheesePizza(CheesePizza):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the CheesePizza interface.
    """

    def interface_a(self):
        print("Chicago Style Cheese Pizza")


class MeatPizza(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class NYStyleMeatPizza(MeatPizza):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the MeatPizza interface.
    """

    def interface_b(self):
        print("NY Style Meat Pizza")


class ChicagoStyleMeatPizza(MeatPizza):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the MeatPizza interface.
    """

    def interface_b(self):
        print("Chicago Style Meat Pizza")


def main():
    for factory in (NYStylePizzaStore(), ChicagoStylePizzaStore()):
        product_a = factory.create_cheese_pizza()
        product_b = factory.create_meat_pizza()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()