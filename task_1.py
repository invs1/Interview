# Function returns reversed int (signed 32-bit)

def reverse_number(num):
    """
    Function which returns reversed 32 bit signed integer
    """
    assert int(num) == num, 'The number must be int only!'
    if num < -2147483648 or num > 2147483647 or num == 0:
        return 0
    else:
        if num > 0:
            return int(str(num)[::-1])
        if num < 0:
            num = num * -1
            num = int(str(num)[::-1]) * -1
            return num

# print(reverse_number(512.1))
