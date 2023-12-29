#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

def calculate_pairwise_distances(adj_list):
    def dfs(vertex, parent, weight):
        distances[start][vertex] = distances[vertex][start] = weight
        for neighbor, w in adj_list[vertex]:
            if neighbor != parent:
                dfs(neighbor, vertex, weight + w)

    n = len(adj_list)
    distances = [[float('inf')] * n for _ in range(n)]
    
    for vertex in range(1, n):
        distances[vertex][vertex] = 0
        for neighbor, weight in adj_list[vertex]:
            distances[vertex][neighbor] = weight

    for start in range(1, n):
        dfs(start, -1, 0)

    final_distances = [row[1:] for row in distances[1:]]
    return final_distances

def optimized_travel_times(adj_list, city_data, pairwise_distances):
    n = len(adj_list) - 1
    min_times = [float('inf')] * (n + 1)
    paths = [-1] * (n + 1)
    
    # Initialize times for all cities
    for city in range(1, n + 1):
        prep_time, speed = city_data[city]
        min_times[city] = pairwise_distances[0][city - 1] / speed + prep_time if city != 1 else 0

    # Adjusted loop to find optimized travel times based on correct implementation
    for i in range(2, n + 1):
        for city in range(2, n + 1):
            if city != i:
                curr_time = min_times[i] + pairwise_distances[city-1][i-1] / city_data[city][1] + city_data[city][0]
                if curr_time < min_times[city]:
                    min_times[city] = curr_time
                    paths[city] = i

    # Correcting the path tracking
    final_paths = {}
    for city in range(2, n + 1):
        path = []
        curr_city = city
        while curr_city != -1:
            path.append(curr_city)
            curr_city = paths[curr_city]
        path.reverse()
        final_paths[city] = path

    last_city = max(range(1, n + 1), key=lambda x: min_times[x])
    return min_times[last_city], final_paths, last_city


with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    city_data = [None] * (N + 1)
    for i in range(1, N + 1):
        city_data[i] = list(map(int, f.readline().strip().split()))
    
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(1, N):
        A, B, S = list(map(int, f.readline().strip().split()))
        adj_list[A].append((B, S))
        adj_list[B].append((A, S))


n = len(adj_list)
pairwise_distances = calculate_pairwise_distances(adj_list)
        
last_time, paths, last_city = optimized_travel_times(adj_list, city_data, pairwise_distances)
curr = last_city

paths[last_city].reverse()
paths[last_city].append(1)
#print(sorted(min_times))
#print(last_time)
#print(paths[last_city])
print(last_time)
print(*paths[last_city])

#path.reverse()
#path.append(1)
#print(last_time)
#print(*path)
    
    

    