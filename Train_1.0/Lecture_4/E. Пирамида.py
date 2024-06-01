with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])
    pairs = [None]*N
    for i in range(N):
        w, h = list(map(int, f.readline().strip().split()))
        pairs[i] = (w, h)

pairs_sorted = sorted(pairs, key= lambda x:x[0], reverse=True)
res = 0
curr_w = pairs_sorted[0][0]
curr_h = pairs_sorted[0][1]

for curr_pair in pairs_sorted:
    if curr_w == curr_pair[0]:
        curr_h = max(curr_h, curr_pair[1])
    else:
        res += curr_h
        curr_w = curr_pair[0]
        curr_h = curr_pair[1]

res += curr_h
print(res)