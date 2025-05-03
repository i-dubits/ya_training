from collections import defaultdict

with (open('input.txt', 'r') as f):
    n, k = list(map(int, f.readline().strip().split()))
    arr = list(map(int, f.readline().strip().split()))

arr = sorted(arr)
n = len(arr)

freq_dict = defaultdict(int)
for el in arr:
    freq_dict[el] += 1

left = 0
right = 0
ans = 0

keys = list(freq_dict.keys())

duplicates_prefix = [0] * (len(keys) + 1)
for i in range(1, len(keys) + 1):
    if freq_dict[keys[i - 1]] >= 2:
        duplicates_prefix[i] = duplicates_prefix[i - 1] + 1
    else:
        duplicates_prefix[i] = duplicates_prefix[i - 1]

for left in range(len(keys)):

    while right < len(keys) and keys[left] * k >= keys[right]:
        right += 1

    distinct_values = (right - 1) - left + 1
    ans += (distinct_values - 1) * (distinct_values - 2) * 3

    if freq_dict[keys[left]] >= 2:
        ans += (distinct_values - 1) * 3
    if freq_dict[keys[left]] >= 3:
        ans += 1

    number_of_duplicates_for_el_greater_than_first = duplicates_prefix[right] - duplicates_prefix[left + 1]
    ans += number_of_duplicates_for_el_greater_than_first * 3

print(ans)

