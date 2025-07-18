from dataclasses import dataclass, field

import sys
sys.setrecursionlimit(100_000)

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())

    graph = [[] for _ in range(N + 1)]

    for _ in range(1, N):
        first, second = map(int, f.readline().strip().split())
        graph[first].append(second)
        graph[second].append(first)


def dfs_longest(graph, node, parent):
    best_dist, best_dist_node = 1, node

    for adj in graph[node]:
        if adj != parent:
            dist, dist_node = dfs_longest(graph, adj, node)
            dist += 1
            if dist > best_dist:
                best_dist = dist
                best_dist_node = dist_node

    return best_dist, best_dist_node

_, start_node = dfs_longest(graph, 1, -1)
distance, _ = dfs_longest(graph, start_node, -1)


print(distance)