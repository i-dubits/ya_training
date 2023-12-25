#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from collections import defaultdict

def dijkstra_algorithm(adj_list, start, end):

    n = len(adj_list)

    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    visited = [False] * n

    while pq:
        curr_dist, curr_vert = heapq.heappop(pq)

        visited[curr_vert] = True

        if curr_vert == end:
            return curr_dist

        for neighbor, weight in adj_list[curr_vert]:
            if not visited[neighbor]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

    return float('inf')


with open('input.txt', 'r') as f:
    N, S, F = list(map(int, f.readline().strip().split()))
    adj_list = [[] for i in range(N + 1)]
    for i in range(1, N + 1):
        str_curr = list(map(int, f.readline().strip().split()))
        for j in range(N):
            if str_curr[j] != -1 and j != i - 1:
                adj_list[i].append((j+1, str_curr[j]))
       
res = dijkstra_algorithm(adj_list, S, F)
if res == float('inf'):
    print(-1)
else:
    print(res)
    
    
    