"""
A working, but hard-to-read Binary Search Tree class in Python.

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

class Tree(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    assert(self.is_tree())

  # Helper functions for updating tree left and right children

  def set_left(self, new_left):
    old_tree = copy.deepcopy(self)
    assert(self.is_tree())
    self.left = new_left
    assert(self.is_tree())
    try:
      assert(self.is_tree())
    except:
      print('reverting')
      self.left = old_tree.left

  def set_right(self, new_right):
    old_tree = copy.deepcopy(self)
    assert(self.is_tree())
    self.right = new_right
    assert(self.is_tree())
    try:
      assert(self.is_tree())
    except:
      print('reverting')
      self.right = old_tree.right
  # Helper function for updating the Tree node's value

  def set_value(self, new_value):
    old_tree = copy.deepcopy(self)
    assert(self.is_tree())
    self.value = new_value
    try:
      assert(self.is_tree())
    except:
      print('reverting')
      self.value = old_tree.value

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
