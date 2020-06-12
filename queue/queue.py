

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying head structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying head structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:
#     def __init__(self, head=None):
#         self.size = 0
#         self.head = [] if head == None else head

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.head.insert(0, value)

#     def dequeue(self):
#         self.size -= 1
#         if len(self.head) == 0:
#             return None
#         else:
#             item = self.head.pop()
#             # print(item)
#             return item


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


# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     # Beginning
#     def enqueue(self, value):
#         self.size += 1
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.get_next() is not None:
#                 current = current.get_next()
#             current.set_next(new_node)

#     # Beginning
#     def dequeue(self):
#         self.size -= 1
#         if not self.head:
#             return None
#         else:
#             value = self.head.get_value()
#             self.head = self.head.get_next()
#             return value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()


# test = Queue()

# print(test.enqueue(1))
# print(test.head)
# print(test.enqueue(2))
# print(test.head)
# print(test.enqueue(3))
# print(test.head)

# print(test.dequeue())
# print(test.head)
# print(test.dequeue())
# print(test.head)
# print(test.dequeue())
# print(test.head)
# print(test.dequeue())
