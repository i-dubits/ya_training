
with (open('input.txt', 'r') as f):
    d = int(f.readline().strip())
    x, y = map(int, f.readline().strip().split())

def closest_vertice(x, y, d):

    ver_to_dist = {}

    dist_A_sq = x**2 + y**2
    dist_B_sq = (x - d)**2 + y**2
    dist_C_sq = x**2 + (y - d)**2

    ver_to_dist[1] = dist_A_sq
    ver_to_dist[2] = dist_B_sq
    ver_to_dist[3] = dist_C_sq

    min_dist = min((dist_A_sq, dist_B_sq, dist_C_sq))

    final_list = []
    for ver_index, dist in ver_to_dist.items():
        if dist == min_dist:
            final_list.append(ver_index)

    if len(final_list) == 1:
        return final_list[0]
    else:
        # We cannot have more than 2 elements in dict
        return min(final_list[0], final_list[1])

def point_inside_tr(x, y, d):
    if y <= -x + d and x >= 0 and y >= 0:
        return 0
    else:
        return 1

if point_inside_tr(x, y, d) == 0:
    print(0)
else:
    res = closest_vertice(x, y, d)
    print(res)


