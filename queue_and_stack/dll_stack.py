from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        self.stack = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        self.stack.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.remove_from_head()
        else:
            return None

    def len(self):
        return self.size
