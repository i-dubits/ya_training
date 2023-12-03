#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp


def pivot_arange(arr, left, right, pivot):
    #piv_indx = randint(left, right)
    #piv_indx = (left + right) // 2
    i = left
    j = right
    
    if not arr:
        return None
    
    while i <= j:
        
        while i < right+1:
            if arr[i] >= pivot:
                break
            i+=1
            
        while j > left - 1:
            if arr[j] < pivot:
                break
            j-=1
            
        if i >= j:
            break

        swap(arr, i, j)
        i+=1
        j-=1
    
    if j == left - 1:
        return None
    return j

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    
    arr = [None]*N
    arr = list(map(int, f.readline().strip().split()))
    pivot = int(f.readline().strip())


ind = pivot_arange(arr, 0, len(arr)-1, pivot)

if ind == None:
    print(0)
    print(len(arr))
else:
    print(ind+1)
    print(len(arr) - ind - 1)




            