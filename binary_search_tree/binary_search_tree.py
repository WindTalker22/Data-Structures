"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # First we check if the new instances value is less than the initial instances value
        if value < self.value:
            # We then check if the initial instances left pointer is equal to None
            if self.left is None:
                # If it is we then instantiate a new instance and set the initial instances left pointer to the new instance
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            # We then check if the initial instances right pointer is equal to None
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # If initial instance value is the new value return true
        if self.value is target:
            return True

        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is not None:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        base = self.value
        if not self.left and not self.right:
            return fn(base)
        if self.left and not self.right:
            return fn(base), self.left.for_each(fn)
        if self.right and not self.left:
            return fn(base), self.right.for_each(fn)
        if self.right and self.left:
            return fn(base), self.right.for_each(fn), self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
