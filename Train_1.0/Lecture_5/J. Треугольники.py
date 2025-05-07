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

ans = 0
equilat_triangles_count = 0

for i in range(n):
    dist_dict = {}
    for j in range(n):
        dist, edge_vec = calc_dist(points[i], points[j])

        if dist not in dist_dict:
            dist_dict[dist] = [edge_vec]
        else:
            dist_dict[dist].append(edge_vec)

    for distance, edge_vec_list in dist_dict.items():
        if len(edge_vec_list) > 1:

            for first in range(len(edge_vec_list)):
                for second in range(first + 1, len(edge_vec_list)):
                    if edge_vec_list[first][0] * edge_vec_list[second][1] - edge_vec_list[first][1] * edge_vec_list[second][0] == 0:
                        pass
                    else:
                        ans += 1
                    diff = tuple((edge_vec_list[first][0] - edge_vec_list[second][0],
                                  edge_vec_list[first][1] - edge_vec_list[second][1]))
                    if calc_vect_length(diff) == distance:
                        equilat_triangles_count += 1

ans -= 2 * (equilat_triangles_count // 3)

print(ans)