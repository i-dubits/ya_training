with (open('input.txt', 'r') as f):
    n, time_per_copy_1, time_per_copy_2 = map(int, f.readline().strip().split())

def check(time_int):

    # We are forced to make the first copy using only one printer
    time_int -= min(time_per_copy_1, time_per_copy_2)

    if time_int < 0:
        return False

    count_1 = time_int // time_per_copy_1
    count_2 = time_int // time_per_copy_2

    if count_1 + count_2 + 1 >= n:
        return True
    else:
        return False

l = 0
r = max(time_per_copy_1, time_per_copy_2) * n

while l < r - 1:
    m = l + (r - l) // 2

    if check(m):
        r = m
    else:
        l = m

if check(l):
    print(l)
else:
    print(r)