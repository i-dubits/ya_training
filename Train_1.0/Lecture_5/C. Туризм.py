
with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])

    prefix_up = [0] * (N + 1)
    prefix_down = [0] * (N + 1)
    prev = 0

    for i in range(1, N + 1):
        x, y = list(map(int, f.readline().strip().split()))
        if y > prev:
            prefix_up[i] = prefix_up[i - 1] + (y - prev)
            prefix_down[i] = prefix_down[i - 1] + 0

        else:
            prefix_up[i] = prefix_up[i - 1] + 0
            prefix_down[i] = prefix_down[i - 1] + (prev - y)

        prev = y

    M = int(f.readline().strip().split()[0])
    for k in range(M):
        res = None
        start, finish = list(map(int, f.readline().strip().split()))
        if start < finish:
            res = prefix_up[finish] - prefix_up[start]
        elif start > finish:
            res = abs(prefix_down[finish] - prefix_down[start])
        elif start == finish:
            res = 0

        print(res)

