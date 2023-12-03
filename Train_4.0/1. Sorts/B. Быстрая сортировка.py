#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint 

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp


def pivot_arange(arr, left, right):
    piv_indx = randint(left, right)
    #piv_indx = (left + right) // 2
    pivot = arr[piv_indx]
    i = left
    j = right
    
    while i <= j:
        
        while i < right+1:
            if arr[i] >= pivot:
                break
            i+=1
            
        while j > left:
            if arr[j] <= pivot:
                break
            j-=1
            
        if i >= j:
            break
        swap(arr, i, j)
        i+=1
        j-=1
    
    return j

def quick_sort(arr, left, right):
    if left + 1 <= right: 
        mid = pivot_arange(arr, left, right)
        quick_sort(arr, left, mid)
        quick_sort(arr, mid+1, right)

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    
    arr = [None]*N
    arr = list(map(int, f.readline().strip().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(*arr)







            