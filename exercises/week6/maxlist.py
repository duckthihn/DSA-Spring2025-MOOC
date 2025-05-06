class MaxList:
    def __init__(self):
        self.list = []
        self.max_stack = []

    def append(self, number):
        self.list.append(number)
        if not self.max_stack or number >= self.max_stack[-1]:
            self.max_stack.append(number)

    def max(self):
        return self.max_stack[-1]


if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max())  # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max())  # 8
