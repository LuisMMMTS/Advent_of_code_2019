#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:47:28 2019

@author: luis
"""

def translate(path):
    final_vector=[]
    inity=0
    initx=0
    for i in path:
        a,b=i[0],int(i[1:])
        for j in range(b):
            if a=="R":
                initx+=1
            if a=="L":
                initx-=1
            if a=="U":
                inity+=1
            if a=="D":
                inity-=1
            final_vector.append((initx,inity))
    return final_vector



f=open("input_day3.txt","r")
a=f.readlines()
f.close()


path_a=a[0].replace(" ","").split(",")
path_b=a[1].replace(" ","").split(",")

translate_a,translate_b=translate(path_a),translate(path_b)

common=[]
j=0
translate_a.sort(key=lambda x: x[0]+x[1])
translate_b.sort(key=lambda x: x[0]+x[1])
quit
for i in translate_a:
    print(j/len(translate_a)*100)
    j+=1
    if i in translate_b:
        common.append(i)
        print(i)
        break
common.sort(key=lambda x: x[0]+x[1])