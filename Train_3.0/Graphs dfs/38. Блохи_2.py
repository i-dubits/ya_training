#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/36/
#

from IPython.core.debugger import set_trace
import sys

from collections import deque


with open('input.txt', 'r') as f:

        
    N, M, S, T, Q = map(int, f.readline().strip().split())
    
    horse_coord = [[] for i in range(Q)]
    
    for i in range(Q):
       x, y = map(int, f.readline().strip().split())
       horse_coord[i] = [x, y] 

matrix = [[-1 for row in range(M+1)] for col in range(N+1) ]
matrix[S][T] = 0

queue = deque()
queue.append([S, T])

while queue:
    x, y = queue.popleft()
    neighs = [[x + 2, y + 1], [x + 2, y - 1], [x - 2, y + 1], [x - 2, y - 1], [x + 1, y + 2], [x - 1, y + 2], [x + 1, y - 2], [x - 1, y - 2]]
    for curr_neigh in neighs:  
        if curr_neigh[0] >= 1 and curr_neigh[0] <= N and curr_neigh[1] >= 1 and curr_neigh[1] <= M:
            if matrix[curr_neigh[0]][curr_neigh[1]] == -1:
                matrix[curr_neigh[0]][curr_neigh[1]] = matrix[x][y] + 1 
                queue.append([curr_neigh[0], curr_neigh[1]])
 
answ = 0
for x, y in horse_coord:
    
    if matrix[x][y] == -1:
        answ = -1
        break
    else:
        answ += matrix[x][y]
        
print(answ)











    
