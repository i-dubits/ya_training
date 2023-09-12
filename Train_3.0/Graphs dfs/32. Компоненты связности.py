#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/31/

from IPython.core.debugger import set_trace
import sys

sys.setrecursionlimit(50000)


with open('input.txt', 'r') as f:
    N, M = list(map(int, f.readline().strip().split()))
    
    adj_list = [[] for i in range(N+1)]
    for k in range(M):
        from_v, to_v = list(map( int, f.readline().strip().split()))
        if from_v != to_v:
            adj_list[from_v].append(to_v)
            adj_list[to_v].append(from_v)
        else:
            adj_list[from_v].append(to_v)
        
marked = [0]*(N+1)
def dfs(vert_ind):
    curr_comp.append(vert_ind)
    marked[vert_ind] = 1
    for w in adj_list[vert_ind]:
        if marked[w] == 0:
            dfs(w)

connect_comp = []

for vert in range(1, N+1):
    curr_comp = []
    if marked[vert] != 1:
        dfs(vert)
        connect_comp.append(curr_comp)
        
print(len(connect_comp))
for comp in connect_comp:
    print(len(comp))
    print(*comp)        
    
