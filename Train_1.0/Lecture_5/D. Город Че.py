with (open('input.txt', 'r') as f):
    n, distance = list(map(int, f.readline().strip().split()))
    a = list(map(int, f.readline().strip().split()))

right = 1
count = 0

for left in range(n):
    while right < n and a[right] - a[left] <= distance:
        right += 1

    count += n - right

print(count)