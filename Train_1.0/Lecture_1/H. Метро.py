
from icecream import ic

with open('input.txt', 'r') as f:
    t1 = int(f.readline())
    t2 = int(f.readline())
    n1 = int(f.readline())
    n2 = int(f.readline())

def calc_min_max_time(t, n):
    min_time = 1 + (t + 1) * (n - 1)
    max_time = (t + 1) * n + t
    return min_time, max_time

min_time_1, max_time_1 = calc_min_max_time(t1, n1)
min_time_2, max_time_2 = calc_min_max_time(t2, n2)

ic(min_time_1, max_time_1)
ic(min_time_2, max_time_2)

intersec_length = min(max_time_1, max_time_2) - max(min_time_1, min_time_2)
ic(intersec_length)
if intersec_length < 0:
    print(-1)
else:
    print(max(min_time_1, min_time_2), min(max_time_1, max_time_2))
    ic(max(min_time_1, min_time_2))
    ic(min(max_time_1, max_time_2))
