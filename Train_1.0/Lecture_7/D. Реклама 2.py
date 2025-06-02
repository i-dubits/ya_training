import copy
from collections import defaultdict
from collections import Counter


distance = 5
with (open('input.txt', 'r') as f):
    segments = []

    N = int(f.readline().strip())
    for i in range(N):
        begin, end = list(map(int, f.readline().strip().split()))
        end -= distance
        if end >= 0 and begin <= end:
            segments.append((begin, end))

DEBUG = True


segments = sorted(segments)
segments_counter = Counter(segments)

coord_to_state_init = defaultdict(list)

for segment in segments:

    coord_to_state_init[segment[0]].append({'type': 'start', 'end_coord': segment[1]})
    coord_to_state_init[segment[1]].append({'type': 'end', 'start_coord': segment[0]})

coord_to_state = {key: coord_to_state_init[key] for key in sorted(coord_to_state_init)}


def preproc(coord_to_state):
    point_to_active_segments = Counter()
    current_active = Counter()

    for coord, event_list in coord_to_state.items():
        for ev in event_list:
            if ev['type'] == 'start':
                current_active[(coord, ev['end_coord'])] += 1

        point_to_active_segments[coord] = current_active.copy()

        for ev in event_list:
            if ev['type'] == 'end':
                if current_active[(ev['start_coord'], coord)] >= 2:
                    current_active[(ev['start_coord'], coord)] -= 1
                else:
                    del current_active[(ev['start_coord'], coord)]

    return point_to_active_segments

point_to_active_segments = preproc(coord_to_state)
if DEBUG:
    print(point_to_active_segments)


def count_customers(coord_1, point_to_active_segments):
    active_seg_coord_1 = point_to_active_segments[coord_1]

    excluded_segments = set(active_seg_coord_1.keys())

    total_count = 0
    coord_2_final = 1_000_000_000_0
    count_1 = sum(active_seg_coord_1.values())

    count_2 = 0
    for coord, event_list in coord_to_state.items():
        count_2_current = 0
        if coord >= coord_1 + distance:
            all_segments = point_to_active_segments[coord].keys()
            for segm in all_segments:
                if segm not in excluded_segments:
                    count_2_current += point_to_active_segments[coord][segm]

        if count_2 < count_2_current:
            count_2 = count_2_current
            coord_2_final = coord

    if count_2 != 0:
        total_count = count_1 + count_2
    else:
        total_count = count_1

    return total_count, coord_1, coord_2_final


window_1 = 0
window_2 = 1_000_000_000_0
total = 0

for coord_1 in coord_to_state.keys():
    total_current, coord_1, coord_2 = count_customers(coord_1, point_to_active_segments)
    if total_current > total:
        total = total_current
        window_1 = coord_1
        window_2 = coord_2

print(total, min(window_1, window_2), max(window_1, window_2))


