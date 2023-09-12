#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/31/

from IPython.core.debugger import set_trace

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
answ = []
def dfs(vert_ind):
    answ.append(vert_ind)
    marked[vert_ind] = 1
    for w in adj_list[vert_ind]:
        if marked[w] == 0:
            dfs(w)
            
dfs(1)
print(len(answ))
print(*sorted(answ))
        
    
