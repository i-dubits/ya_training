with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])
    arr_dict = {}
    res = 0
    for i in range(N):
        curr_turtle = tuple(map(int, f.readline().strip().split()))

        if curr_turtle not in arr_dict:
            arr_dict[curr_turtle] = 1
        else:
            arr_dict[curr_turtle] += 1

        if (curr_turtle[0] + curr_turtle[1] == N - 1 and arr_dict[curr_turtle] == 1
                and curr_turtle[0] >= 0 and curr_turtle[1] >= 0):
            res += 1

print(res)