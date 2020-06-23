def square(number):
    if number <= 0 or number > 64:
        raise ValueError('Number is invalid')
    return 2 ** (number - 1)


def total():
    total = 1
    for i in range(1, 64):
        total += 2 ** i
    return total
