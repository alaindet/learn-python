class AveragerClass:

    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, num: int) -> float:
        self.total += num
        self.count += 1
        return self.total / self.count


avg1 = AveragerClass()
print(avg1.add(1))  # 1.0
print(avg1.add(2))  # 1.5
print(avg1.add(42))  # 15.0


def averagerClosure():
    nums: list[int] = []

    def add(num: int) -> float:
        nums.append(num)
        return sum(nums) / len(nums)

    return add


avg2 = averagerClosure()
print(avg2(1))  # 1.0
print(avg2(2))  # 1.5
print(avg2(42))  # 15.0


def averagerClosure2():
    total = 0
    count = 0

    def add(num: int) -> float:
        nonlocal total
        nonlocal count
        total += num
        count += 1
        return total / count

    return add


avg3 = averagerClosure2()
print(avg3.__closure__)  # Some address of the cell
print(avg3.__code__.co_freevars)  # ('count', 'total')
print(avg3(1))  # 1.0
print(avg3(2))  # 1.5
print(avg3(42))  # 15.0
