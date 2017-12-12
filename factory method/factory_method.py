"""
Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer
instantiation to subclasses.
"""

import abc


class PizzaStore(metaclass=abc.ABCMeta):
    """
    Declare the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory
    method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object.
    """

    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass


class NYPizzaStore(PizzaStore):
    """
    Override the factory method to return an instance of a
    NYPizzaStore.
    """

    def _factory_method(self):
        return NYPizza()


class ChicagoPizzaStore(PizzaStore):
    """
    Override the factory method to return an instance of a
    ChicagoPizzaStore.
    """

    def _factory_method(self):
        return ChicagoPizza()


class Pizza(metaclass=abc.ABCMeta):
    """
    Define the interface of objects the factory method creates.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class NYPizza(Pizza):
    """
    Implement the Product interface.
    """

    def interface(self):
        return "NY Style Pizza"


class ChicagoPizza(Pizza):
    """
    Implement the Product interface.
    """

    def interface(self):
        return "Chicago Style Pizza"


def main():
    concrete_pizza_store_ny = NYPizzaStore()
    print(concrete_pizza_store_ny.product.interface())

    concrete_pizza_store_chicago = ChicagoPizzaStore()
    print(concrete_pizza_store_chicago.product.interface())

if __name__ == "__main__":
    main()