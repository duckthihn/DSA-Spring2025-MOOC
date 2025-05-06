# class RepeatList:
#     def __init__(self):
#         self.numbers = set()
#         self.repeat_status = False
#
#     def append(self, number):
#         if number in self.numbers:
#             self.repeat_status = True
#         self.numbers.add(number)
#
#     def repeat(self):
#         return self.repeat_status

class RepeatList:
    def __init__(self):
        self.list = []
        self.set = set()

    def append(self, number):
        self.list.append(number)
        self.set.add(number)

    def repeat(self):
        return False if len(self.list) == len(self.set) else True


if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat())  # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat())  # False

    numbers.append(2)
    print(numbers.repeat())  # True

    numbers.append(5)
    print(numbers.repeat())  # True
