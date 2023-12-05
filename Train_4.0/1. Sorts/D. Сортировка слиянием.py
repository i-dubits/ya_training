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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = (len(arr)-1) // 2
    
    arr1 = merge_sort(arr[0: mid+1])
    arr2 = merge_sort(arr[mid+1: len(arr)])
    res = merge(arr1, arr2)
    
    return res

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    arr_1 = [None]*N
    arr_1 = list(map(int, f.readline().strip().split()))



res = merge_sort(arr_1)
print(*res)





