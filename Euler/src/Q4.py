'''
Created on Dec 17, 2014

@author: ljiang

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math
import timeit
#O(n)=(n^2+n)/2
def findLargestPalindrome():
    palin=0
    for i in xrange(100,1000):
        for j in xrange(100,i+1):
            product=str(i*j)
            reversed_product=product[::-1]
            #if i == 993 and j==913:
                #pass
            for char,reversed_char in zip(product,reversed_product):
                if char != reversed_char:
                    break
            else:
                if palin < i*j: 
                    palin=i*j
    return palin        

#O(n)=6*n+n^(3/2)
def findLargestPalindrome2():
    for num in xrange(999*999,10000,-1):
        str_num=str(num)
        rev_str_num=str_num[::-1]
        for char,reversed_char in zip(str_num,rev_str_num):
            if char != reversed_char:
                break
        else:
            for factor in xrange(999,int(math.sqrt(num))-1,-1):
                if num%factor==0:
                    #factor2=num/factor
                    return num


            
print findLargestPalindrome()    
print findLargestPalindrome2()
                
print timeit.timeit(findLargestPalindrome,'from __main__ import findLargestPalindrome',number=5) 
print timeit.timeit(findLargestPalindrome2,'from __main__ import findLargestPalindrome2',number=5)                   
                    
                