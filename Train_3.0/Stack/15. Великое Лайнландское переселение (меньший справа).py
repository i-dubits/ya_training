#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/15/

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())    
    input_seq = list(map(int, f.readline().strip().split()))
   
my_stack = []
answ_arr = [-1]*len(input_seq)

for i in range(len(input_seq)):
    
    while my_stack and my_stack[-1]['value'] > input_seq[i]:
        prev = my_stack.pop()
        answ_arr[prev['ind']] = i
        
    curr_dict = {'ind':i, 'value':input_seq[i]}
    my_stack.append(curr_dict)
        

print(*answ_arr)