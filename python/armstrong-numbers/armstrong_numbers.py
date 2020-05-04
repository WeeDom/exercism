def is_armstrong_number(number):
    nums = [ int(i) for i in str(number)]
    total = 0
    for i in nums:
        total += i ** len(nums)

    return total == number
