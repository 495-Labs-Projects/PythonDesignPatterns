"""
This is the Pizza Store example without using Factory Method. There
is an issue here with code that does not allow for individual stores
to define their own implementation of each type of pizza.

As we can see, each implementation of the pizza store needs to implement
its own version of pizza, but are unable to here. This means that 
we can't have different location stores make different styles of pizza.

This can be fixed by using factory method to encapsulate different
styles of pizza so that each location can make a different implementation
of making pizza.
"""

import abc


class PizzaStore(metaclass=abc.ABCMeta):

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
        return Pizza() 


class ChicagoPizzaStore(PizzaStore):
    """
    Override the factory method to return an instance of a
    ChicagoPizzaStore.
    """

    def _factory_method(self):
        return Pizza() 


class Pizza():
    """
    Define the interface of objects the factory method creates.
    """

    def interface(self):
        return "Generic Pizza"

def main():
    concrete_pizza_store_ny = NYPizzaStore()
    print(concrete_pizza_store_ny.product.interface() + " made in New York.") 

    concrete_pizza_store_chicago = ChicagoPizzaStore()
    print(concrete_pizza_store_chicago.product.interface() + " made in Chicago.")

if __name__ == "__main__":
    main()