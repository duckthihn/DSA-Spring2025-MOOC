class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        return self.stack.append(x)

    def top(self):
        if len(self.stack) == 0:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def pop(self, x):
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        return self.stack.pop(x)


a = Stack()

arr = [1, 2, 3, 4, 5]

for x in arr:
    a.push(x)
    print(a.top())
