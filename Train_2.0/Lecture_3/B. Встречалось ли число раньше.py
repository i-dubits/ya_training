
with (open('input.txt', 'r') as f):
    arr = list(map(int, f.readline().strip().split()))

my_set = set()

for el in arr:
    if el not in my_set:
        print('NO')
        my_set.add(el)
    else:
        print('YES')