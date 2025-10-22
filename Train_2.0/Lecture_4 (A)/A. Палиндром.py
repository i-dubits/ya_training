
from collections import Counter

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    count_dict = Counter(f.readline().strip())

keys_sorted = sorted(count_dict.keys())

first_part_list = []

for key in keys_sorted:
    if count_dict[key] > 1:
        if count_dict[key] % 2 == 0:
            first_part_list.extend( [key] * (count_dict[key] // 2) )
            count_dict[key] = 0
        else:
            first_part_list.extend([key] * ((count_dict[key] - 1) // 2) )
            count_dict[key] = 1

second_part_list =  first_part_list[::-1]
for key in keys_sorted:
    if count_dict[key] == 1:
        first_part_list.append(key)
        break

full_str = ''.join(first_part_list) + ''.join(second_part_list)
print(full_str)