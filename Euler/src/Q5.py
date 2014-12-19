'''
Created on Dec 17, 2014

@author: ljiang

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import timeit
from math import *

#O(n)=n^2
def LCM():
    mul=20
    while True:
        for div in xrange(20,0,-1):
            if mul%div!=0:
                mul+=20
                break
        else: return mul

#O(n)=n
def LCM2():
    lcm=1
    for i in xrange(2,21):
        lcm=lcm*i/GCD2(i,lcm)
    return lcm

#O(n)=n
def GCD(a,b):
    if a>b:
        small=b
    else: small=b
    for div in xrange(small,1,-1):
        if a%div==0 and b%div == 0:
            return div
#O(n)=1
def GCD2(a,b):
    if a>b:
        while b != 0:
            a,b=b,a%b
            gcd=a
    else: 
        while a != 0:
            b,a=a,b%a
            gcd=b
    return gcd

#find a list of prime number for number series from 1 to 20
def findPrimeList():
    prime=[2]
    for num in xrange(3,21):
        for i in xrange(2,int(sqrt(num))+1):
            if num%i==0:
                break
        else: prime.append(num)
    return prime

def LCM3():
    lcm=1
    for p in findPrimeList():
        a=int(log10(20)/log10(p))
        lcm=lcm*(p**a)
    return lcm

#print findPrimeList()
print LCM3()
#print GCD(20*4,15*4)
#print GCD2(20*4,15*4)
print LCM2()
#print LCM()
print timeit.timeit(LCM3,'from __main__ import LCM3',number=100) 
print timeit.timeit(LCM2,'from __main__ import LCM2',number=100) 
#print timeit.timeit(LCM,'from __main__ import LCM',number=1)   