#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:56:26 2019

@author: luis
"""

def has_adjacent_equal(n):
    iold=None
    for i in str(n):
        if i==iold:
            return True
        iold=i
    return False

def has_two_adjacent_equal(n):
    digits={}
    for i in str(n):
        try: 
            digits[i]+=1
        except:
            digits[i]=1
    if 2 in digits.values():
        return True
    return False
            
        
    return False

def digits_increase(n):
    iold=str(n)[0]
    for i in str(n):
        if i<iold:
            return False
        iold=i
    return True

passwords=[]
for i in range(245182,790572):
    if i>=100000 and i<1000000 and has_adjacent_equal(i) and digits_increase(i) and has_two_adjacent_equal(i):
        passwords.append(i)
print(len(passwords))