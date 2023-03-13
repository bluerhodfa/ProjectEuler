#!/usr/bin/env python3

"""
projecteuler.net Problem 7

Find the 10001st prime

Some useful facts:
1 is not a prime.
All primes except 2 are odd.
All primes greater than 3 can be written in the form 6k+/-1.
n .
The consequence for primality testing of a number n is: if we cannot find a number f less than
Any number n can have only one primefactor greater than
or equal n that divides n then n is prime: the only primefactor of n is n itself



"""
import datetime
import math

def is_prime(n, div=2):
    if div> int(math.sqrt(n)): return True
    if n% div == 0:
        return False
    else:
        div+=1
        return is_prime(n,div)


now = datetime.datetime.now()

until = int(10002)

primelist=[]
i=1;
while len(primelist)<until:
    if is_prime(i):
        primelist.insert(0,i)
        i+=1
    else: i+=1



print("Project Euler - Problem 7")
print("What is the 10001st prime number?")
print("Answer = ", max(primelist))
finish = datetime.datetime.now()
print("It took your computer", finish - now , "secs to calculate it")
