"""
A working, clean Binary Search Tree class in Python.

The Binary Search Tree data structure maintains the following invariants:
  1. For any node to the left of a given point in the tree, such node has a value smaller than the given point.
  2. For any node to the right of a given point in the tree, such node has a value larger than the given point.
  3. Any node has between 0 and 2 subtree children (inclusive).

For the purpose of this implementation, we will use a Python class `Tree` with the following attributes:
  A. Tree.left is a Tree class or None
  B. Tree.right is a Tree class or None
  C. Tree.value is an integer (not a float, String, or any other Python datatype)

The following invariants of this tree class must be tested:
  1. Left and right subchildren of a node follow the ordering invariant of the general BST data structure (points 1 and 2 above).
  2. Left and right subchildren of a node are either Tree class instances or None (points A and B above).
  3. The value of a non-None node must be an integer.
"""
import copy

def assert_invariants(func):
  def wrapper(*args):
    experiment_tree = args[0]
    update = args[1]
    old_tree = copy.deepcopy(experiment_tree)
    assert(experiment_tree.is_tree())
    func(experiment_tree, update)
    try:
      assert(experiment_tree.is_tree())
    except:
      print('reverting')
      experiment_tree.value = old_tree.value
      experiment_tree.left = old_tree.left
      experiment_tree.right = old_tree.right
  return wrapper

class Tree(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    assert(self.is_tree())

  # Helper functions for updating tree left and right children
  @assert_invariants
  def set_left(self, new_left):
    self.left = new_left

  @assert_invariants
  def set_right(self, new_right):
    self.right = new_right
  # Helper function for updating the Tree node's value

  @assert_invariants
  def set_value(self, new_value):
    self.value = new_value    

  # Generalized function to check tree invariants
  def is_tree(self):
    if (not isinstance(self, Tree)):
      return False
    if (not(type(self.value) == int)):
      return False
    if (self.left and self.right):
      return ((self.left.value < self.value) and 
             (self.right.value > self.value) and
             (self.left.is_tree()) and
             (self.right.is_tree()))
    elif (self.left):
      return ((self.left.value < self.value) and 
             (self.left.is_tree()))
    elif (self.right):
      return ((self.right.value > self.value) and
             (self.right.is_tree()))
    else:
      return True
