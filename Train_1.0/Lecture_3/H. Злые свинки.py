with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])

    x_set = set()

    for i in range(N):
        curr_x_y = tuple(map(int, f.readline().strip().split()))
        if curr_x_y[0] not in x_set:
            x_set.add(curr_x_y[0])

print(len(x_set))