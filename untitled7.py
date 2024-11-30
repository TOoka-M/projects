# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 06:17:19 2024

@author: TechnoShip
"""
num=int(input("enter your numbers to calculate the sum : "))
sum=0
count = 0
for i in range (num):
    x=int(input("enter value : "))

    if x> 0 :
        sum+=x
        count+=1
avg=sum/count
print(sum , avg)
