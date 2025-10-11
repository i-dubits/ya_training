
def day_period_to_set(first_day, period, N):
    res_set = set()
    curr_day = first_day
    while curr_day <= N:
        if (curr_day - 6) % 7 != 0 and curr_day % 7 != 0:
            res_set.add(curr_day)
        curr_day += period

    return res_set

with open('input.txt', 'r') as f:
    N, K = map(int, f.readline().strip().split())

    pairs = []
    for i in range(K):
        first_day, period = map(int, f.readline().strip().split())
        pairs.append((first_day, period))

strike_set = set()
for pair in pairs:
    strike_set = strike_set.union( day_period_to_set(pair[0], pair[1], N) )

print(len(strike_set))
