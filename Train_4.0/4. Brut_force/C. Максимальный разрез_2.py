
def precompute_vertex_weights(adj_list):
    vertex_weights = [0] * len(adj_list)
    for u, neighbors in enumerate(adj_list):
        vertex_weights[u] = sum(weight for _, weight in neighbors)
    return vertex_weights

def calculate_edge_weight_with_bitmask(adj_list, bitmask):
    total_weight = 0
    N = len(adj_list)
    for u in range(N):
        if bitmask & (1 << u):
            for v, weight in adj_list[u]:
                if not (bitmask & (1 << v)):
                    total_weight += weight
    return total_weight

def find_max_weight_distribution_with_bitmask(N, adj_list):
    max_weight = 0
    best_bitmask = 0
    for bitmask in range(1, 1 << N):
        weight = calculate_edge_weight_with_bitmask(adj_list, bitmask)
        if weight > max_weight:
            max_weight = weight
            best_bitmask = bitmask
    return max_weight, best_bitmask

def format_distribution_with_bitmask(N, best_bitmask):
    distribution = ['2' if best_bitmask & (1 << i) else '1' for i in range(N)]
    return ' '.join(distribution)

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    adj_list = [[] for _ in range(N)]
    for i in range(N):
        weights = list(map(int, f.readline().strip().split()))
        for j, weight in enumerate(weights):
            if weight != 0 and i != j:
                adj_list[i].append((j, weight))

max_weight, best_bitmask = find_max_weight_distribution_with_bitmask(N, adj_list)

result = format_distribution_with_bitmask(N, best_bitmask)
print(max_weight)
print(result)

