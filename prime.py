#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Provides is_prime(x) and prime_between(x, y)."""
import unittest


def is_prime(x):
    """Returns True if x is prime, otherwise returns False."""
    if x < -1:
        for i in range(-2, x, -1):
            if x % i == 0:
                return False
    elif x in [-1, 0, 1]:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


def prime_between(x, y):
    """Returns all the prime numbers between x and y inclusive."""
    primes = []
    if x > y:
        orig_x = x
        x = y
        y = orig_x
    for number in range(x, y + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def main():
    print prime_between(0, 100)
    print prime_between(0, -100)
    print prime_between(-100, 0)
    print prime_between(100, 0)
    print prime_between(3, 89)
    print prime_between(-3, -89)


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        for prime_number in [-2, -3, -5, -7, -11, 2, 3, 5, 7, 11]:
            self.r = is_prime(prime_number)
            self.assertTrue(self.r, 
                    "is_prime(%i) returned %r" % (prime_number, self.r))
        for non_prime in [-10, -9, -8, -6, -4, -1, 0, 1, 4, 6, 8, 9, 10]:
            self.r = is_prime(non_prime)
            self.assertFalse(self.r, 
                    "is_prime(%i) returned %r" % (non_prime, self.r))


class TestPrimeBetween(unittest.TestCase):

    def test_prime_between(self):
        self.test_cases = [
            # x, y, expected_result
            (0, 11, [2, 3, 5, 7, 11]),
            (11, 0, [2, 3, 5, 7, 11]),
            (0, -11, [-11, -7, -5, -3, -2]),
            (-11, 0, [-11, -7, -5, -3, -2]),
            (-3, -11, [-11, -7, -5, -3]),
            (-11, -3, [-11, -7, -5, -3]),
        ]
        for x, y, expected_result in self.test_cases:
            self.r = prime_between(x, y)
            self.assertEquals(expected_result, self.r, 
                "prime_between(%i, %i) returned %r" % (x, y, self.r))


if __name__ == '__main__':
    main()
    unittest.main()
