
with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])
    a = list(map(int, f.readline().strip().split()))

    M = int(f.readline().strip().split()[0])
    b = list(map(int, f.readline().strip().split()))

    min_diff = None
    curr_diff = abs(a[0] - b[0])

    second = 1
    for first in range(N):
        second -= 1
        if second < M:
            curr_diff = abs(a[first] - b[second])
        while second < M and abs(a[first] - b[second]) <= curr_diff:
            curr_diff = abs(a[first] - b[second])
            second += 1

        if not min_diff or min_diff > curr_diff:
            min_diff = curr_diff
            opt_a_ind = first
            opt_b_ind = second - 1

            opt_a = a[first]
            opt_b = b[second - 1]


        if min_diff == 0:
            break

#print(min_diff)
#print(f'opt_a_ind: {opt_a_ind}')
#print(f'opt_b_ind: {opt_b_ind}')
#print(f'opt_a: {opt_a}')
#print(f'opt_b: {opt_b}')

print(f'{opt_a} {opt_b}')