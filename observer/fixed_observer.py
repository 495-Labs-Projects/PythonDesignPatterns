"""
An easier to manage system of observers using Python

Here, we want a parent to be able to push allowance updates to their children to update their wallets.

We can best capture this relationship by interactions between two classes, helping with explainability and maintenance
"""

class Parent(object):
  def __init__(self):
    self.children = []

  def add_child(self, child):
    self.children.append(child)

  def update_children_wallets(self):
    for child in self.children:
      child.update_wallet()
      print(child.name + ' now has $' + str(child.wallet))

class Child(object):
  def __init__(self, name, allowance=5, wallet=0):
    self.name = name
    self.allowance = allowance
    self.wallet = wallet

  def update_wallet(self):
    self.wallet += self.allowance

dana = Child('Dana', allowance=10, wallet=20)
elliot = Child('Elliot')
mackenzie = Child('Mackenzie', allowance = 8)

parent = Parent()
parent.add_child(dana)
parent.add_child(elliot)
parent.add_child(mackenzie)
parent.update_children_wallets()
