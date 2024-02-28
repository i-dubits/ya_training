


with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))
    target = int(f.readline().strip())

curr_cand = None
min_distance = 10_000

for i in range(N):
    curr_distance = abs(arr[i] - target)
    if curr_distance < min_distance:
        curr_cand = arr[i]
        min_distance = curr_distance

print(curr_cand)