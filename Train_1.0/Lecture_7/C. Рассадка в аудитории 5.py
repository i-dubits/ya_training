from collections import defaultdict

with (open('input.txt', 'r') as f):
    N, distance = map(int, f.readline().strip().split())
    students = list(map(int, f.readline().strip().split()))

x_coords = sorted(students)
l = 0
r = 0

free_labels = []
coord_to_label_map = defaultdict(int)

for l in range(len(x_coords)):

    while r < len(x_coords) and x_coords[r] - x_coords[l] <= distance:

        if len(free_labels) != 0:
            coord_to_label_map[x_coords[r]] = free_labels.pop()
        else:
            coord_to_label_map[x_coords[r]] = r - l + 1

        r += 1

    free_labels.append( coord_to_label_map[x_coords[l]] )

print(len(set(coord_to_label_map.values())))
print(' '.join([str(coord_to_label_map[x_coord]) for x_coord in students]))