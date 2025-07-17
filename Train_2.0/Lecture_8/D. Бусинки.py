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


    # tree = [[] for i in range(1, N + 1)]
    # for _ in range(1, N):
    #     first, second = map(int, f.readline().strip().split())
    #     tree[first].append(second)


def single_pass(graph, node, curr_l, max_l, visited):

    visited[node] = True

    for adj_node in graph[node]:
        if not visited[adj_node]:
            proposed_max_l = single_pass(graph, adj_node, curr_l + 1, max_l, visited)
            max_l = max(max_l, proposed_max_l)

    max_l = max(max_l, curr_l)
    return max_l

def longest_path_node(graph, node, curr_l, max_l, max_node, visited):

    visited[node] = True

    for adj_node in graph[node]:
        if not visited[adj_node]:
            proposed_max_l, proposed_max_node = (
                longest_path_node(graph, adj_node, curr_l + 1, max_l, max_node, visited))

            if max_l < proposed_max_l:
                max_l = max(max_l, proposed_max_l)
                max_node = proposed_max_node

    if max_l < curr_l:
        max_l = max(max_l, curr_l)
        max_node = node

    return max_l, max_node

# visited = [False] * (N + 1)
# print(single_pass(graph, 2, 1, 1, visited))

visited = [False] * (N + 1)
_, max_node = longest_path_node(graph, 1, 1, 1, None, visited)

visited = [False] * (N + 1)
longest = single_pass(graph, max_node, 1, 1, visited)
print(longest)

# longest = 1
# for node in range(1, N + 1):
#
#     visited = [False] * (N + 1)
#     curr_pass_l = single_pass(graph, node, 1, 1, visited)
#     longest = max(longest, curr_pass_l)
#
# print(longest)


