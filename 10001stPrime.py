#!/usr/bin/env python3

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
