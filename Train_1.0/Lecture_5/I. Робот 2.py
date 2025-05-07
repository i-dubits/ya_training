with (open('input.txt', 'r') as f):
    k = int(f.readline())
    arr = f.readline().strip().split()[0]

# Number of valid strings that end in the current pointer location
cnt_valid_end = 0
ans = 0

for i in range(k, len(arr)):

    if arr[i] == arr[i - k]:
        cnt_valid_end += 1
        ans += cnt_valid_end

    else:
        cnt_valid_end = 0

print(ans)