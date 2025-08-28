
with (open('input.txt', 'r') as f):
    N, K = map(int, f.readline().strip().split())
    arr = list(map(int, f.readline().strip().split()))

res = max(arr) - min(arr)
print(res)