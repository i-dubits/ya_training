from collections import defaultdict

with (open('input.txt', 'r') as f):
    n, k = list(map(int, f.readline().strip().split()))
    arr = f.readline().strip()

n = len(arr)
freq_dict = defaultdict(int)
curr_len = 0

max_len = 0
first_max_len = None

first = 0
second = 0

for first in range(len(arr)):
    while second < n and (arr[second] not in freq_dict or freq_dict[arr[second]] < k):
        freq_dict[arr[second]] += 1
        second += 1

    curr_len = (second - 1) - first + 1
    if max_len < curr_len:
        max_len = curr_len
        first_max_len = first

    freq_dict[arr[first]] -= 1

print(max_len, first_max_len + 1)