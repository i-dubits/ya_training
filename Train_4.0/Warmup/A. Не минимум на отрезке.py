#!/usr/bin/env python3
# -*- coding: utf-8 -*-

seq = []
with open('input.txt', 'r') as f:
    N, M = list(map(int, f.readline().strip().split()))
    seq = list(map(int, f.readline().strip().split()))
    
    my_stack = []
    answ = [-1]*len(seq)
    for i, el in enumerate(seq):
        while my_stack and  my_stack[-1][1] != el:
            stack_ind, stack_val = my_stack.pop()
            answ[stack_ind] = i
        
        my_stack.append((i, el))
        
    for i in range(M):
        L, R = list(map(int, f.readline().strip().split()))
        
        if answ[L] == -1 or answ[L] > R:
            print('NOT FOUND')
        else:
            other = seq[answ[L]]
            current = seq[L]
            res = max(other, current)
            print(res)
            #print(seq[res])
    
