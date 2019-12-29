#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:22:07 2019

@author: luis
"""


def run_code(a):
    for i in range(0,len(a),4):
        if int(a[i])==99:
            break
        if int(a[i])==1:
            a[int(a[i+3])]=int(a[int(a[i+1])])+int(a[int(a[i+2])])
        elif int(a[i])==2:
            a[int(a[i+3])]=int(a[int(a[i+1])])*int(a[int(a[i+2])])
    return a[0]        


f=open('input.txt','r')
a=f.readlines()
f.close()
a=a[0].replace(" ","").replace('\n',"").split(",")

for i in range (100):
    for j in range(100):
        a[1]=i
        a[2]=j
        if run_code(a)==19690720:
            print(100*i+j)
            
def run_code(a):
    for i in range(0,len(a),4):
        if int(a[i])==99:
            break
        if int(a[i])==1:
            a[int(a[i+3])]=int(a[int(a[i+1])])+int(a[int(a[i+2])])
        elif int(a[i])==2:
            a[int(a[i+3])]=int(a[int(a[i+1])])*int(a[int(a[i+2])])
    return a[0]        
