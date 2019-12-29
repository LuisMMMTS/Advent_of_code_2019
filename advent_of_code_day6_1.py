#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:55:28 2019

@author: luis
"""

def create_map(array):
    orbits={}
    for i in array:
        i=i.split(")")
        if i[1] in orbits.keys():
            j=orbits[i[1]]
            j.append(i[0])
            orbits[i[1]]=j
        else:
            orbits[i[1]]=[i[0]]
    return orbits

def create_map2(array):
    orbits={}
    for i in array:
        i=i.split(")")
        if i[0] in orbits.keys():
            j=orbits[i[0]]
            j.append(i[1])
            orbits[i[0]]=j
        else:
            orbits[i[0]]=[i[1]]
    return orbits

def total_orbits2(orbits,i):
    total=0
    if i  not in orbits.keys():
        return 0
    else:
        total=len(orbits[i])
        for j in orbits[i]:
            total+=total_orbits2(orbits,j)
        return total
    
def total_orbits(orbits):
    total=0
    for i in orbits.keys():
        total+=total_orbits2(orbits,i)
    return total



f=open("input_day6.txt","r")
array=f.readlines()
f.close()
for i in range(len(array)):
    array[i]=array[i].split('\n')[0]

objects_orbiting=create_map(array)
orbit_object=create_map2(array)
total=total_orbits(objects_orbiting)
total2=total_orbits(orbit_object)
print(total,total2)
