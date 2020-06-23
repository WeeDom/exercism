import re


def is_valid(isbn):
    digits = list(isbn.replace('-', ''))
    if len(digits) != 10 or not ''.join(digits[:-1]).isnumeric():
        return False
    if not digits[-1].isnumeric():
        if digits[-1].lower() != 'x':
            return False
    digits[-1] = (digits[-1], 10)[digits[-1].lower() == 'x']

    total = 0
    cnt = 0
    for i in range(10, 1, -1):
        total = total + (int(digits[cnt]) * i)
        cnt = cnt + 1
    import pdb; pdb.set_trace()
    return total % 11 == 0
