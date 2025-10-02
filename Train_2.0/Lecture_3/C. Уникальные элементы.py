from collections import defaultdict


with (open('input.txt', 'r') as f):
    arr = list(map(int, f.readline().strip().split()))

my_dict = defaultdict(int)
for el in arr:
    my_dict[el] += 1

res = []
for el, val in my_dict.items():
    if val == 1:
        res.append(el)

print(*res)
