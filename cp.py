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

<<<<<<< HEAD
"""Multiplies fractions from two tuples and returns the result in one tuple"""
def multiplyFractions(a, b):
    return [a[0] * b[0], a[1] * b[1]]

"""Adds two fractions together"""
def addFractions(a, b):
    denom = lcm(a[1], b[1])
    return [denom / a[1] * a[0] + denom / b[1] * b[0], denom]

"""Reduces a fraction to it's simples form"""
def reduceFraction(a):
    b = gcd(a[0], a[1])
    return [a[0] / b, a[1] / b]

 """Returns all prime factors of number"""
def PrimeFactors(n):
    #Returns factors of n

    primeList = []
    d = 2
    while n != 0:
        if n % d == 0:
            primeList.append(d)
            n /= d
        else:
            d += 1
        if d*d > n:
            if n > 1:
                primeList.append(n)
            break
    return primeList
"""Returns number of divisors"""
def NumberOfDivisors(n):
    #Returns the number of divisors of n

    factors = PrimeFactors(n)
    tmp = factors[0]
    res,count = 1, 0

    for x in range(len(factors)):
        if factors[x] != tmp:
            tmp = factors[x]
            res *= (count+1)
            count = 1
            if x == len(factors):
                res *= 2
        else:
            count += 1
    if count > 0:
        res *= (count+1)
    return res

"""Checks if number is palindrome"""
def isPalindrome(n):
    reversed = 0
    tmp = n
    while tmp != 0:
        reversed*= 10
        reversed += tmp % 10
        tmp /= 10
    if n == reversed: return True
    return False
=======
>>>>>>> 7c853dfed9621fb3f8c32bcf9ca78f1baf7675b8
