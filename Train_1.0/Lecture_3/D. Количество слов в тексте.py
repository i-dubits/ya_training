lines = []
with open('input.txt', 'r') as f:
    lines.append(tuple(f.readline().strip().split()))
    while lines[-1]:
        lines.append(tuple(f.readline().strip().split()))

my_set = set()
for line in lines[:-1]:
    my_set = my_set.union(set(line))

print(len(my_set))
