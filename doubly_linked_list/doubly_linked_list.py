"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Create new node
        new_node = ListNode(value)
        # Increment the length by 1
        self.length += 1
        # If there is no head or tail
        if not self.head and not self.tail:
            # Then we set the new node to the head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # We set the new nodes next pointer to the old head
            new_node.next = self.head
            # We then  set the old heads previous pointer to the new node
            self.head.prev = new_node
            # We then update the head to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # Check to see if list is empty
        if not self.head:
            return None
        # We want the value of the removed node returned so we set it to a variable
        value = self.head.value
        # We use the delete method on the head
        self.delete(self.head)
        # We then return the deleted value
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # Create new node
        new_node = ListNode(value)
        # Increment length by 1
        self.length += 1
        # Check if there is no head or tail and if there isn't DLL is empty
        if not self.head and not self.tail:
            # If DLL is empty we set the new node to the head and tail
            self.head = new_node
            self.tail = new_node
        # If DLL is not empty
        else:
            # We then set the old tails pointer to the new node
            # The new node is already set to none
            self.tail.next = new_node
            # We then set the new nodes previous to the old tail
            new_node.prev = self.tail
            # We then update the tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # Check to see if list is empty
        if not self.tail:
            return None
        # We want the value of the removed node returned so we set it to a variable
        value = self.tail.value
        # We use the delete method on the tail
        self.delete(self.tail)
        # We then return the deleted value
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # Check to see if the node is already equal to the head
        if node is self.head:
            return
        # We want to capture the value of the node
        value = node.value
        # We want to delete the node from its current position
        self.delete(node)
        # We then want to add the node to the beginning of the list
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # Check to see if the node is already equal to the tail
        if node is self.tail:
            return
        # We want to capture the value of the node
        value = node.value
        # We want to delete the node from its current position
        self.delete(node)
        # We then want to add the node to the end of the list
        self.add_to_tail(value)
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # We check if the DLL is empty
        if not self.head and not self.tail:
            return None
        # WE then decrement the length of the DLL by 1
        self.length -= 1
        # We then check if DLL has one element
        # If there is we remove it by setting head and tail pointers to none
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # We then check if the node to delete is the head
        # If it is we set the head pointer to node.next
        # We then delete the node connection
        elif self.head is node:
            self.head = node.next
            node.delete()
        # We then check if the node to delete is the tail
        # If it is we set the tail pointer to node.prev
        # We then delete the node connection
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # There are more than two nodes
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        current = self.head

        max = self.head.value

        while current is not None:
            if current.value > max:
                max = current.value

            current = current.next
        return max
