#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/12/


with open('input.txt', 'r') as f:
   br_string = f.readline().strip()
   
br_stack = []
res = None

br_map = {')':'(', ']':'[', '}':'{'}

for i in range(len(br_string)):
    curr = br_string[i]
    
    if curr in ['(', '[', '{']:
        br_stack.append(curr)
        
    elif curr in [')', ']', '}']:
        if br_stack:
            if br_map[curr] != br_stack.pop():
                res = False
                break
        else:
            res = False
            break            

if not br_stack and res != False:
    print('yes')
else:
    print('no')
















