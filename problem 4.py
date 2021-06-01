"""Problem Statement- Pronic Numbers
We should divide the total number into substrings and we should verify each num is pronic num or not if pronic we should print that num

Pronic: means it is a multiple of two consecutive integers
"""
import math

num_string = input()
subset_num_string = set()
outnum = []
for i in range(len(num_string)):
    for j in range(i,len(num_string)+1):
        if num_string[i:j]=='':
            pass
        else:
            subset_num_string.add(int(num_string[i:j]))
subset_num_string = sorted(list(subset_num_string))
for num in subset_num_string:
    for val in range(1,int(math.sqrt(num))+1):
        if val*(val+1)==num:
            outnum.append(num)
print(outnum)