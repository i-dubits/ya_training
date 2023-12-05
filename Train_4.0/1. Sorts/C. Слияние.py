#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge(arr1, arr2):
    i = 0
    j = 0
    
    res = []
    
    while i < len(arr1) or j < len(arr2):
        
        if i == len(arr1) and j < len(arr2):
            res.append(arr2[j])
            j+=1
            continue
            
        if i < len(arr1) and j == len(arr2):
            res.append(arr1[i])
            i+=1
            continue
        
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
            
    return res

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    arr_1 = [None]*N
    arr_1 = list(map(int, f.readline().strip().split()))
    
    M = int(f.readline().strip())
    arr_2 = [None]*M
    arr_2 = list(map(int, f.readline().strip().split()))



res = merge(arr_1, arr_2)
print(*res)