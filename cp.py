"""
Competitive Programming Library for Python

Functions:
    #Primes:
        isPrime(n)
        sieve(n)
    #Fibonacci:
        fib(n)

Authors: Glitch
https://github.com/RuNnNy/CP
"""

import math

"""Primality check that iterates through all integers below the square root of
the number being checked and makes sure it's not divisable by any of them"""
def isPrime(n):
    if n <= 1:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False

    for i in range(3, math.sqrt(n) + 1, 2):
        if n % i is 0:
            return False
    return True

"""Returns a Sieve of Eratosthenes. Generates all prime numbers below n"""
def sieve(n):
    prime = [True] * n + 1
    prime[0], prime[1] = False, False

    for i in range(2, math.sqrt(n) + 1):
        if prime[i]:
            for k in range(i * i, n + 1, i):
                prime[k] = False
    return prime

# Fast doubling Fibonacci algorithm
#
# Copyright (c) 2013 Nayuki Minase
# All rights reserved. Contact Nayuki for licensing.
# http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms

# Returns F(n)
def fib(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# Returns a tuple (F(n), F(n+1))
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

