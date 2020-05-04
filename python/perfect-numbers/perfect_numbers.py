def classify(num):
    if int(num) <= 0:
        raise ValueError('number was not a valid, positive integer')
# a bit annoying that i have to adjust a var name for a linter, but...
    res = sum([i for i in range(1, num + 1) if num % i == 0 and i != num])
    if res > num:
        return 'abundant'
    if res < num:
        return 'deficient'
    if res == num:
        return 'perfect'
