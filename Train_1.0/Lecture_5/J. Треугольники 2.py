from collections import defaultdict

def calc_dist(point_1, point_2):
    edge_vec = tuple((point_1[0] - point_2[0], point_1[1] - point_2[1]))
    dist = (edge_vec[0])**2 + (edge_vec[1])**2

    return dist, edge_vec

def calc_vect_length(vec):
    return vec[0]**2 + vec[1]**2

def minus_edge_vect(edge_vect):
    return tuple((edge_vect[0] * (-1), edge_vect[1] * (-1)))

with (open('input.txt', 'r') as f):
    n = int(f.readline())
    points = [None] * n
    for i in range(n):
        points[i] = tuple(map(int, f.readline().strip().split()))

edges_vects = set()

bad_triangles = 0
ans = 0

for i in range(n):
    dist_dict = {}
    for j in range(n):
        if i != j:
            dist, edge_vec = calc_dist(points[i], points[j])

            if dist not in dist_dict:
                dist_dict[dist] = set((edge_vec,))
            else:
                if minus_edge_vect(edge_vec) in dist_dict[dist]:
                    bad_triangles += 1
                dist_dict[dist].add(edge_vec)

    for dist, edge_vec_set in dist_dict.items():
        set_size = len(edge_vec_set)
        if set_size > 1:
            ans += set_size * (set_size - 1) // 2

ans -= bad_triangles
print(ans)