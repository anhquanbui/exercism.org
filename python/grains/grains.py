def square(number):
    return 2 ** (number - 1)


def total():
    return sum(square(i) for i in range(1, 65))
