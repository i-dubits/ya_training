
with open('input.txt', 'r') as f:
    N = int(f.readline().strip())

dp_0 = [None]*40
dp_01 = [None]*40
dp_11 = [None]*40
res = [None]*40

res[1] = 2
res[2] = 4
res[3] = 7

dp_0[3] = 4
dp_01[3] = 2
dp_11[3] = 1

if N <= 3:
    print(res[N])
else:
    k = 4
    while k <= N:
        dp_0[k] = dp_0[k-1] + dp_01[k-1] + dp_11[k-1]
        dp_01[k] = dp_0[k-1]
        dp_11[k] = dp_01[k-1]

        res[k] = dp_0[k] + dp_01[k] + dp_11[k]
        k += 1
    print(res[N])

