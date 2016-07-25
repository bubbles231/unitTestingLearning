#!/usr/bin/env python3
# coding=utf-8
"""
Finding out how to effectively use unit tests in my code using an example
from:
https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
"""


import unittest
from primes import is_prime


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`"""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()
