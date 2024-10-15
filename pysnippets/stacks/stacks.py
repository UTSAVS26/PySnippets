class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    def push(self, item):
        if self.top == self.size - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item
    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.top -= 1
        return item
    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
         
        return self.stack[self.top]
   
        return self.stack[self.top]

