'''
Created on Dec 15, 2014

@author: ljiang

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math
import timeit

#need a decorator to run timeit for function with parameters:
def decorator(function,*args,**kwargs):
    def wrapper():
        return function(*args,**kwargs)
    return wrapper


def largestPrimeFactor(num):
    for n in xrange(num-1,1,-1):
        if num % n == 0:
            for m in xrange(n-1,1,-1):
                if n%m==0:
                    break
                if m==2:
                    return n 
                continue

def largestPrimeFactor2(num):
    factors=[None,None]
    largest_factor=0
    for small_div in xrange(2,int(math.sqrt(num))+1):
        if num % small_div ==0:
            large_div=num/small_div
            factors[0]=small_div
            factors[1]=large_div
            for i in xrange(2):
                isprime = True                
                for n in xrange(int(math.sqrt(factors[i])),1,-1):
                    if factors[i]%n==0:
                        isprime = False
                        break
                if isprime and factors[i]>largest_factor:
                    largest_factor=factors[i]                                    
    return largest_factor


#limit to n^(1/2)*n^(1/4)*n^(1/8)*...*n^(1/n), converge to n.  
def largestPrimeFactorRecursive(num):
    for small_div in xrange(2,int(math.sqrt(num))+1):
        if num % small_div ==0:
            large_div=num/small_div
            x=largestPrimeFactorRecursive(large_div)
            if x == None:
                return large_div
            else: return x
    
def largestPrimeFactorIterative(num):
    factor=2
    while factor < int(math.sqrt(num))+1:
        if num % factor ==0:
            num=num/factor
            largest_div=factor
        else: factor+=1
    if num>largest_div:
        largest_div=num
    return largest_div


            
print largestPrimeFactor(13195)
print largestPrimeFactor2(600851475143)
print largestPrimeFactorRecursive(600851475143)
print largestPrimeFactorIterative(13195)


wrapper=decorator(largestPrimeFactor,600851475143)
wrapper2=decorator(largestPrimeFactor2,600851475143)
wrapper3=decorator(largestPrimeFactorRecursive,600851475143)
wrapper4=decorator(largestPrimeFactorIterative,600851475143)

#print timeit.timeit(wrapper,'from __main__ import largestPrimeFactor',number=1)
print timeit.timeit(wrapper2,'from __main__ import largestPrimeFactor2',number=1)
print timeit.timeit(wrapper3,'from __main__ import largestPrimeFactorRecursive',number=10000)
print timeit.timeit(wrapper4,'from __main__ import largestPrimeFactorIterative',number=10000)

                