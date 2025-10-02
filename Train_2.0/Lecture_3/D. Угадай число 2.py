with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())

    yes_list = []
    no_list = []

    while True:
        curr_line = f.readline().strip()
        if curr_line[0] == 'H':
            break

        curr_list = list(map(int, curr_line.split()))
        next_line = f.readline().strip()

        if next_line[0] == 'Y':
            yes_list.append(curr_list)
        elif next_line[0] == 'N':
            no_list.extend(curr_list)
        else:
            print(f'Something is wrong with line: {next_line}')

if len(yes_list) != 0:
    yes_set = set(min(yes_list, key = lambda x: len(x)))
    for el in yes_list:
        yes_set = yes_set.intersection(set(el))
else:
    yes_set = set()

no_set = set(no_list)

if len(yes_set) != 0:
    target = yes_set.difference(no_set)
else:
    target = set(range(1, N + 1)).difference(no_set)

print(*sorted( target ) )