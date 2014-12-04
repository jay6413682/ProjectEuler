'''
Created on Nov 24, 2014

@author: ljiang
'''
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import timeit
def q1():
    x=0
    for y in xrange(1,1000):
        #print y
        if y%3==0 or y%5==0:
            x+=y
            #print x
            
    print x
    return x

def div(n,m):
    return (int(m/n)+1)*int(m/n)/2*n

def q1_2():
    return div(3,999)+div(5,999)-div(15,999)


print timeit.timeit(q1,'from __main__ import q1',number=1000)
print timeit.timeit(q1_2,'from __main__ import q1',number=10000)