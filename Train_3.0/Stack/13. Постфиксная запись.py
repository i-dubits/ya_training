#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/13/

with open('input.txt', 'r') as f:
   input_str = f.readline().strip().split()
   
my_stack = []
for i in range(len(input_str)):
    curr = input_str[i]
    
    if curr in ['-', '+', '*']:
        if my_stack:
            first = my_stack.pop()
            second = my_stack.pop()
            
            if curr == '-':
                res_curr = second - first
            elif curr == '+':
                res_curr = second + first
            elif curr == '*':
                res_curr = second * first
            
            my_stack.append(res_curr)
    else:
        my_stack.append(curr)
        
print(my_stack[-1])