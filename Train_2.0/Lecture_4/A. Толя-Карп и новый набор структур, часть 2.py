
from collections import defaultdict


with (open('input.txt', 'r') as f):
    n = int(f.readline().strip())
    my_dict = defaultdict(int)
    for i in range(n):
        key, value = map(int, f.readline().strip().split())
        my_dict[key] += value

sorted_keys_list = sorted(my_dict)
ans = []
for key in sorted_keys_list:
    curr = str(key) + ' ' + str(my_dict[key])
    ans.append(curr)

print('\n'.join(ans))