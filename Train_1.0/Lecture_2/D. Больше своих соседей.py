with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))

res = []
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        res.append(arr[i])

print(len(res))