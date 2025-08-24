
with (open('input.txt', 'r') as f):
    arr_1 = map(int, f.readline().strip().split())
    arr_2 = map(int, f.readline().strip().split())

ans = len(set(arr_1).intersection(set(arr_2)))
print(ans)

