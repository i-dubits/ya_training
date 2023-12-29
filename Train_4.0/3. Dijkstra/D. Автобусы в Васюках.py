#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

def earliest_arrival_dijkstra(adj_list, start, end):


    arrival_times = [float('inf')] * (len(adj_list) + 1)
    arrival_times[start] = 0

    pq = [(0, start)]  # (arrival time, village)

    while pq:
        curr_time, curr_village = heapq.heappop(pq)

        if curr_village == end:
            return curr_time

        for next_village, dep_time, arr_time in adj_list[curr_village]:
            if dep_time >= curr_time:
                if arr_time < arrival_times[next_village]:
                    arrival_times[next_village] = arr_time
                    heapq.heappush(pq, (arr_time, next_village))

    return float('inf') if arrival_times[end] == float('inf') else arrival_times[end]



with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    S, F = list(map(int, f.readline().strip().split()))
    R = int(f.readline().strip())

    adj_list = [[] for _ in range(N + 1)]
    for _ in range(R):
        
        depart, depart_time, arr, arr_time = list(map(int, f.readline().strip().split()))
        adj_list[depart].append((arr, depart_time, arr_time))
        
       
res = earliest_arrival_dijkstra(adj_list, S, F)
if res == float('inf'):
    print(-1)
else:
    print(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    