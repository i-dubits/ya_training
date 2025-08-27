
with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

res = sum(arr) - max(arr)
print(res)