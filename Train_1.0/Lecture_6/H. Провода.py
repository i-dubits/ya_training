with (open('input.txt', 'r') as f):
    n, k = map(int, f.readline().strip().split())
    arr = [None] * n
    for i in range(n):
        arr[i] = int(f.readline().strip())

arr = sorted(arr)

def check(length):
    count = 0
    for i in range(len(arr)):
        count += arr[i] // length
        if count >= k:
            return True

    return False

l = 1
r = max(arr)

while l < r - 1:
    m = l + (r - l) // 2

    if check(m):
        l = m
    else:
        r = m

if check(r):
    print(r)
elif check(l):
    print(l)
else:
    print(0)