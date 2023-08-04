"""
2^15 = 32768 and the sum of its digits is
3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

"""
Logic: Just a normal brute force approach
"""

def power_digit_sum(base: int, exponent: int) -> int:
    """
    function: find the sum of the digits of the number base ^ exponent
    params: base of type int and exponent of type int
    returns: the sum of the digits of the number base ^ exponent of type int
    """
    result = base ** exponent
    digit_sum = sum(int(digit) for digit in str(result))
    return digit_sum

print(power_digit_sum(2, 1000))