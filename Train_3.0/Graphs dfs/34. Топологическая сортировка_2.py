#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/34/
# 

from IPython.core.debugger import set_trace
import sys
from collections import deque

sys.setrecursionlimit(5000)


with open('input.txt', 'r') as f:
    N, M = list(map(int, f.readline().strip().split()))
    
    adj_list = [[] for i in range(N+1)]
    for k in range(M):
        from_v, to_v = list(map( int, f.readline().strip().split()))
        if from_v != to_v:
            adj_list[from_v].append(to_v)
            #adj_list[to_v].append(from_v) # for undirected graph
        else:
            adj_list[from_v].append(to_v)
        
answ = []
if_cycle = False


def dfs():
    global if_cycle
    while call_stack: 
        vert_ind = call_stack[-1]
        if vert_color_list[vert_ind] == -1:
            vert_color_list[vert_ind] = 1
            for w in adj_list[vert_ind]:
                if vert_color_list[w] == -1:
                    call_stack.append(w)
                elif vert_color_list[w] == 1 and w in call_stack:
                    if_cycle = True
                    return
        elif vert_color_list[vert_ind] == 1:
            answ.append(vert_ind)
            call_stack.pop()
            vert_color_list[vert_ind] = 2       
        else:
            call_stack.pop()
vert_color_list = [-1]*(N+1)
for vert in range(1,N+1):
    if vert_color_list[vert] == -1:
        call_stack = deque()
        call_stack.append(vert)
        dfs()

if if_cycle:
    print(-1)
else:
    print(*answ[::-1])

    
