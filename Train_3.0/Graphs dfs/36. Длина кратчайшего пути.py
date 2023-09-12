#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/36/
#

from IPython.core.debugger import set_trace
import sys

from collections import deque


with open('input.txt', 'r') as f:
    N = int(f.readline().strip().split()[0])
    
    adj_list = [[] for i in range(N+1)]
    for i in range(1, N+1):
        row = [int(item) for item in f.readline().strip().split()]
        adj_list[i] = [ind+1 for ind, el in enumerate(row) if el != 0]
        
    first_vert, sec_vert = map(int, f.readline().strip().split())


def bfs(vert_ind):

    queue = deque()
    queue.append(vert_ind)
       
    edge_to = [-1] * (N+1)
    distances = [-1] * (N+1)
    
    distances[vert_ind] = 0
    
    while queue:
        curr_vert = queue.popleft()
        for w in adj_list[curr_vert]:
            
            if distances[w] == -1: # not visited
                distances[w] = distances[curr_vert] + 1 
                edge_to[w] = curr_vert
                queue.append(w)
            
    return distances, edge_to

distances, edge_to = bfs(first_vert)

print(distances[sec_vert])













    
