from singly_linked_list import LinkedList
import sys
sys.path.append(
    '/Users/stephensaciolo/projects/computer-science/Data-Structures/stack/singly_linked_list.py')

"""
A stack is a value structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack:
#     def __init__(self, storage=None):
#         self.size = 0
#         self.storage = [] if storage == None else storage

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         self.size -= 1
#         if len(self.storage) == 0:
#             return None
#         else:
#             item = self.storage.pop()
#             return item

# <---------First Attempt with LL---------->

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next


# class Stack:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     # Beg
#     def push(self, value):
#         self.size += 1
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.get_next() is not None:
#                 current = current.get_next()
#             current.set_next(new_node)
#             self.tail = new_node

#     # Beg
#     def pop(self):
#         self.size -= 1
#         if not self.head:
#             return None
#         else:
#             value = self.head
#             for i in range(self.size):
#                 value = value.get_next()
#             self.tail = value.get_value()
#             if self.tail == self.head.get_value():
#                 lastValue = self.head
#                 self.head = None
#                 return lastValue.get_value()
#             return value.get_value()


# Nested Classes 2nd Attempt with LL
class IsEmptyError(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, value, _next):
            self.value = value
            self._next = _next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        if self.size <= 0:
            self.size = 0
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            # raise IsEmptyError('This stack is empty, therefore cannot pop')
            return None
        else:
            head = self.head.value
            self.head = self.head._next
            self.size -= 1
        return head


# test = Stack()


# test.push(1)
# print(len(test))
# test.push(2)
# print(len(test))
# test.push(3)
# print(len(test))
# test.pop()
# print(len(test))
# test.pop()
# print(len(test))
# test.pop()
# print(len(test))
# test.pop()
