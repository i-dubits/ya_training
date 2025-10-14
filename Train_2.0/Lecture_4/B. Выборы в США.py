
from collections import defaultdict

with (open('input.txt', 'r') as f):
    my_dict = defaultdict(int)

    curr_line = f.readline().strip()
    while curr_line != '':
        key, value = curr_line.split()
        value = int(value)
        my_dict[key] += value
        curr_line = f.readline().strip()

sorted_keys_list = sorted(my_dict)
ans = []
for key in sorted_keys_list:
    curr = key + ' ' + str(my_dict[key])
    ans.append(curr)

print('\n'.join(ans))
