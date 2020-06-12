from collections import deque


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

    def __repr__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        # First we check if the new value is less than the initial instances value
        if value < self.value:
            # We then check if the initial instances left pointer is equal to None
            if self.left is None:
                # If it is we then instantiate a new instance and set the initial instances left pointer to the new instance
                self.left = BSTNode(value)
            else:
                # We hop over the node that the instance is pointing to and insert new node recursively
                self.left.insert(value)
        else:
            # If the value of the instance was greater
            # We then check if the  instances right pointer is equal to None
            if self.right is None:
                # If it is we then instantiate a new instance and set the initial instances right pointer to the new instance
                self.right = BSTNode(value)
            else:
                # We hop over the node that the instance is pointing to and insert new node recursively
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # If initial instance value is the same as the new value return true
        if self.value is target:
            return True
        # We then decide which direction to traverse down the tree
        # If this is true we go left and check the values
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
        # If this is true we go right and check the values
        elif self.value < target:
            if self.right is not None:
                return self.right.contains(target)
        else:
            # If neither of the previous conditions are met we return False
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
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

 # Print the value of every node, starting with the given node,
 # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = []
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            node = stack.pop(-1)
            print(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

        # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
