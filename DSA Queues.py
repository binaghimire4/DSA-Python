#a queue is a linear data structure that follows a "first-in-first-out"(FIFO)principle.
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

