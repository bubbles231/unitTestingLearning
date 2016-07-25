# coding=utf-8
"""
Finding out how to effectively use unit tests in my code using an example
from:
https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
"""


def is_prime(number):
    """Return True if prime"""
    if number in (0, 1):
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


def print_next_prime(number):
    """Print the closest prime number larger than `number`"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
