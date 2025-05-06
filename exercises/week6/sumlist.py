# class SumList:
#     def __init__(self):
#         self.list = []
#
#     def append(self, number):
#         self.list.append(number)
#
#     def sum(self, a, b):                         O(n)
#         total = 0
#         for i in range(a, b + 1):
#             total += self.list[i]
#
#         return total
class SumList:
    def __init__(self):
        self.prefix_sum = [0]

    def append(self, number):
        self.prefix_sum.append(self.prefix_sum[-1] + number)

    def sum(self, a, b):
        return self.prefix_sum[b + 1] - self.prefix_sum[a]


if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4))  # 15
    print(numbers.sum(1, 1))  # 2
    print(numbers.sum(1, 3))  # 9
    print(numbers.sum(2, 3))  # 7
    print(numbers.sum(0, 3))  # 10

    numbers.append(1)
    print(numbers.sum(0, 5))  # 16
    print(numbers.sum(5, 5))  # 1
