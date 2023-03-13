#!/usr/bin/env python3

"""

Project Euler.net Problem 3
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(w):
    return w == w[::-1]

max_p = 0
for n in range(100,999):
    for m in range(100,999):
        if is_palindrome(str( n * m )) == True:
            if ( n * m ) > max_p: max_p = n * m

print("Largest palindrome from product of two three digit umbers is ",  max_p)
