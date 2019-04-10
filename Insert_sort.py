# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:50:33 2019

@author: chjia
"""

def sort(A):
    
    for j in range(1,len(A)):
        key=A[j]
        i=j
        while key<A[i-1] and i-1>=0:
            A[i]=A[i-1]
            i=i-1
        A[i]=key
            
A=[35, 21, 32, 56]
sort(A)
print A  