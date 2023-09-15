#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/14/


from IPython.core.debugger import set_trace

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    seq = list(map(int, f.readline().strip().split()))
    
curr_search = 1

my_stack = []
answ = []

answ_bin = True

#set_trace()
for i in range(len(seq)):
    curr_el = seq[i]
    if curr_el != curr_search:
        my_stack.append(curr_el)
    else:
        answ.append(curr_el)
        curr_search += 1
        while my_stack:
            curr_el = my_stack[-1]
            if curr_el == curr_search:
                answ.append(curr_el)
                my_stack.pop()
                curr_search += 1
            else:
                break

if my_stack:
    print('NO')
else:
    print('YES')