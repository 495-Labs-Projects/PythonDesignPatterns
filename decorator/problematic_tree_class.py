"""
A working, but unclean Binary Search Tree class in Python.

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

class Tree(object):
  def __init__(self, value, left=None, right=None):
    assert(type(value) == int)
    self.value = value
    self.left = left
    self.right = right

  # Helper functions for updating tree left and right children

  def set_left(self, new_left):
    assert(isinstance(new_left, Tree) or (new_left == None))
    assert((new_left == None) or (new_left.value < self.value))
    self.left = new_left

  def set_right(self, new_right):
    assert(isinstance(new_right, Tree) or (new_right == None))
    assert((new_right == None) or (new_right.value > self.value))
    self.right = new_right

  # Helper function for updating the Tree node's value

  def set_value(self, new_value):
    assert(type(new_value) == int)
    assert((self.left == None) or (self.left.value < value))
    assert((self.right == None) or (self.right.value > value))
    self.value = new_value
