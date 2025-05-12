

with (open('input.txt', 'r') as f):
    n, k = list(map(int, f.readline().strip().split()))
    arr_1 = list(map(int, f.readline().strip().split()))
    arr_2 = list(map(int, f.readline().strip().split()))

arr_1_count = set(arr_1)

for el in arr_2:
    if el in arr_1_count:
        print('YES')
    else:
        print('NO')