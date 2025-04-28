with (open('input.txt', 'r') as f):
    N, K = list(map(int, f.readline().strip().split()))
    a = list(map(int, f.readline().strip().split()))

left = 0
right = 0

count = 0
curr_sum = 0

for left in range(N):
    if left != 0 and left <= right:
        curr_sum -= a[left - 1]

    right = max(right, left)
    while right < N and curr_sum + a[right] <= K:
        curr_sum += a[right]
        if curr_sum == K:
            count += 1
        right += 1

print(count)


