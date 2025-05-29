from collections import defaultdict

with (open('input.txt', 'r') as f):
    N, min_distance = map(int, f.readline().strip().split())

    students = list(map(int, f.readline().strip().split()))

DISTANCE_END = 1
STUDENT_POSITION = -1

events = []

for st in students:
    events.append((st, STUDENT_POSITION))
    events.append((st + min_distance, DISTANCE_END))

events.sort()

free_labels = []
global_max_label = 0

student_pos_to_label_map = defaultdict(int)

for ev in events:

    if ev[1] == STUDENT_POSITION:

        if len(free_labels) == 0:
            curr_label = global_max_label + 1
            student_pos_to_label_map[ev[0]] = curr_label

            global_max_label += 1

        else:
            curr_label = free_labels.pop()
            student_pos_to_label_map[ev[0]] = curr_label

    if ev[1] == DISTANCE_END:
        new_free_label = student_pos_to_label_map[ev[0] - min_distance]
        free_labels.append(new_free_label)

print(len(set(student_pos_to_label_map.values())))
print(' '.join([str(student_pos_to_label_map[st]) for st in students]))