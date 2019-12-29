#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:17:11 2019

@author: luis
"""

def run_code(a):
    i=0
    while i< len(a):
        parameter1,parameter2,parameter3,op=opcode(a[i])
        if op not in [3,99]:
            parameter1=value_in_parameter(parameter1, 1, a,i)
        if op not in [3,4,99]:
            parameter2=value_in_parameter(parameter2, 2, a,i)
        
        
        if op==99:
            break
        elif op==1:
            a[int(a[i+3])]=parameter1+parameter2
        elif op==2:
            a[int(a[i+3])]=parameter1*parameter2
        elif op==3:
            a[int(a[i+1])]=int(input())
            i+=2
            continue
        elif op==4:
            print(parameter1)
            i+=2
            continue
        elif op==5:
            if parameter1!=0:
                i=parameter2
                continue
            i+=3
            continue
        elif op==6:
            if parameter1==0:
                i=parameter2
                continue
            i+=3
            continue
        elif op==7:
            if parameter1<parameter2:
                a[a[i+3]]=1
            else:
                a[a[i+3]]=0
        elif op==8:
            if parameter1==parameter2:
                a[a[i+3]]=1
            else:
                a[a[i+3]]=0
        else:
            return 1
        i+=4
    return a[0]


def opcode(code):
    code=str(code)
    parameter1,parameter2,parameter3,op=0,0,0,0
    op=int(code[-2:])
    if len(code)>=3:
        parameter1=int(code[-3])
        if len(code)>=4:
            parameter2=int(code[-4])
            if len(code)>=5:
                parameter3=int(code[-5])
    return parameter1,parameter2,parameter3,op
                
def value_in_parameter(parameter,parameter_nr,a,i):
    if parameter==1:
        parameter=a[i+parameter_nr]
    elif parameter==0:
        parameter=a[a[i+parameter_nr]]
    return parameter

f=open("advent_of_code_day5.txt","r")
a=f.readlines()
f.close()
a=a[0].replace(" ","").split(",")
a = list(map(int, a))
run_code(a)
