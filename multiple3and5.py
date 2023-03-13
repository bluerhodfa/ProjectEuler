#!/usr/bin/env python3


"""
projetceuler.net

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
import datetime
import math

now = datetime.datetime.now()
t = 0
n = 1

while ( n < 1000):
    if ( n % 3  == 0 or n % 5 == 0) : t = t + n
    n = + n + 1
print( "The sum of all the multiples of 3 or 5 below 1000 is", t)

print( sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0))

finish = datetime.datetime.now()
print( "It took your computer", finish - now , "secs to calculate it")
