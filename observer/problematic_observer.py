"""
A difficult to manage system of observers using Python

Here, we want a parent to be able to push allowance updates to their children to update their wallets.

Note that this does not properly capture the essence of the parent/child relationship
"""

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

children = [dana, elliot, mackenzie]

def update_allowance(children):
  for child in children:
    child.update_wallet()
    print(child.name + ' now has $' + str(child.wallet))

update_allowance(children)
