from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        self.queue = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.queue.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
