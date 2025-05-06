# class PermutationTracker:
#     def __init__(self):
#         self.numbers = []
#         self.max_num = 0
#
#     def append(self, number):
#         self.numbers.append(number)
#         if number > self.max_num:
#             self.max_num = number
#
#     def check(self):
#         if len(self.numbers) != self.max_num:
#             return False
#
#         for i in range(1, self.max_num + 1):
#             if i not in self.numbers:
#                 return False
#
#         return True

# class PermutationTracker:
#     def __init__(self):
#         self.numbers = []
#         self.max_num = 0
#         self.unique_num = 0
#
#     def append(self, number):
#         if number not in self.numbers:
#             self.numbers.append(number)
#             self.max_num = max(self.max_num, number)
#         else:
#             self.unique_num += 1
#
#     def check(self):
#         if len(self.numbers) != self.max_num:
#             return False
#         if self.unique_num != 0:
#             return False
#
#         return True

class PermutationTracker:

    def __init__(self):
        self.numbers = set()
        self.count = 0
        self.min = None
        self.max = None

    def append(self, number):
        self.numbers.add(number)
        self.count += 1

        if self.count == 1:
            self.min = self.max = number
        else:
            self.min = min(self.min, number)
            self.max = max(self.max, number)

    def check(self):
        if self.count != len(self.numbers):
            return False
        if self.min != 1 or self.max != self.count:
            return False
        return True


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check())  # True

    tracker.append(4)
    print(tracker.check())  # False

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(3)
    print(tracker.check())  # True

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(5)
    print(tracker.check())  # False
