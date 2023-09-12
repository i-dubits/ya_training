#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/33/
# bipartite graph

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
vert_type_list = [-1]*(N+1)
answ = ''
def dfs(vert_ind, vert_curr_type):
    
    #set_trace()
    global answ
    marked[vert_ind] = 1
    for w in adj_list[vert_ind]:
        
        if vert_type_list[w] == -1:
            vert_type_list[w] = 3 - vert_curr_type
            #print(vert_type_list[w])
        elif vert_type_list[w] != 3 - vert_curr_type:
            answ = 'NO'
            #print(answ)
            return
        if marked[w] == 0:
            dfs(w, 3 - vert_curr_type)

vert_type_list[1] = 1       
for vert in range(1, N+1):
    if marked[vert] != 1:
        dfs(vert, 1)

if answ != 'NO':
    print('YES')
else:
    print('NO')

    
