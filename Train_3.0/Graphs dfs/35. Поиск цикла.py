#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/35/
# cycle in undirected graph

from IPython.core.debugger import set_trace
import sys

from collections import deque

sys.setrecursionlimit(5000)


with open('input.txt', 'r') as f:
    N = int(f.readline().strip().split()[0])
    
    adj_list = [[] for i in range(N+1)]
    for i in range(1, N+1):
        row = [int(item) for item in f.readline().strip().split()]
        adj_list[i] = [ind+1 for ind, el in enumerate(row) if el != 0]
        

def dfs(vert_ind, prev_vert):
    
    global if_cycle
    global cycle_start
    cycle_list.append(vert_ind)
    #set_trace()    
    for w in adj_list[vert_ind]:
        if vert_color_list[w] == -1:
            vert_color_list[w] = 1
            dfs(w, vert_ind)
        elif vert_color_list[w] == 1 and w != prev_vert:
            if if_cycle == True:
                return #vert_ind
            else:
                if_cycle = True
                
                cycle = list(cycle_list)[cycle_list.index(w):]
                print('YES')
                print(len(cycle))
                print(*cycle)
        
    vert_color_list[vert_ind] = 2
    if cycle_list:
        cycle_list.pop()

if_cycle = False
cycle_start = -1
vert_color_list = [-1]*(N+1)
for vert in range(1,N+1):
    if vert_color_list[vert] == -1:
        if if_cycle:
            break
        else:
            if_cycle = False
            cycle_list = deque()
            #cycle_list.append(vert)
            vert_color_list[vert] = 1
            dfs(vert, -1)
           

if not if_cycle:
    print('NO')

    
