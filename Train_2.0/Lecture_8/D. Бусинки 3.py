from dataclasses import dataclass, field

from collections import deque
import sys
sys.setrecursionlimit(100_000)

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())

    graph = [[] for _ in range(N + 1)]

    for _ in range(1, N):
        first, second = map(int, f.readline().strip().split())
        graph[first].append(second)
        graph[second].append(first)


def bfs_longest(graph, node):
    queue = deque([node])
    dist = [-1] * ( len(graph) + 1 )

    dist[node] = 1

    while queue:
        node = queue.popleft()

        for adj in graph[node]:
            if dist[adj] == -1:
                dist[adj] = dist[node] + 1
                queue.append(adj)

    max_dist = max(dist[1:])
    max_node = dist.index(max_dist)

    return max_dist, max_node


# print(bfs_longest(graph, 1))

_, start_node = bfs_longest(graph, 1)
distance, _ = bfs_longest(graph, start_node)
print(distance)