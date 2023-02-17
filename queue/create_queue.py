from node import Node


class Queue:

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

queue = Queue(1)

queue.enqueue(2)

queue.enqueue(3)

print(queue.dequeue().value)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(3)
queue.print_queue()