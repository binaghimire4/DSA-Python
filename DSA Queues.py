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
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

Q = Queue()
Q.enqueue('A')
Q.enqueue('B')
Q.enqueue('C')
print("Queue:", Q.queue)
print("dequeue:", Q.dequeue())
print("peek:", Q.peek())
print("isEmpty:", Q.size)

