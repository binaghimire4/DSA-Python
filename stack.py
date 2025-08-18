#A stack is a linear data structure that is LIFO principle. This means the last element added to the stack is the first one to be removed

class stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
myStack = stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ",myStack.stack)
print("pop:", myStack.pop())
print("peek:", myStack.peek())
print("isEmpty:", myStack.isEmpty())
print("Size:", myStack.size())