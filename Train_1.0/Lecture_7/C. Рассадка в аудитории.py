from collections import defaultdict

DISTANCE_END = 1
STUDENT_POSITION = -1

with (open('input.txt', 'r') as f):
    N, min_distance = map(int, f.readline().strip().split())

    students = list(map(int, f.readline().strip().split()))

events = []

for st in students:
    events.append((st, STUDENT_POSITION))
    events.append((st + min_distance, DISTANCE_END))

events.sort()

labels_pool = []
student_pos_to_label_map = defaultdict(int)

for ev in events:
    if ev[1] == STUDENT_POSITION:
        if len(labels_pool) == 0:
            labels_pool.append(1)
            student_pos_to_label_map[ev[0]] = labels_pool[-1]
        else:
            min_label = min(labels_pool)
            if min_label > 1:
                student_pos_to_label_map[ev[0]] = min_label - 1
                labels_pool.append(min_label - 1)
            else:
                current_expected = min(labels_pool)
                find_el = False
                for label in sorted(labels_pool):
                    if current_expected != label:
                        student_pos_to_label_map[ev[0]] = current_expected
                        labels_pool.append(current_expected)
                        find_el = True
                        break
                    current_expected += 1

                if not find_el:
                    max_label = max(labels_pool)
                    student_pos_to_label_map[ev[0]] = max_label + 1
                    labels_pool.append(max_label + 1)



    if ev[1] == DISTANCE_END:
        labels_pool.pop(0)

print( len( set(student_pos_to_label_map.values()) ) )
print(' '.join([str(student_pos_to_label_map[st]) for st in students]))
