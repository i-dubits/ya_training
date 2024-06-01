with (open('input.txt', 'r') as f):
    n = int(f.readline().strip().split()[0])
    _limits = list(map(int, f.readline().strip().split()))
    # start numbering with 1
    limits = [None]
    limits.extend(_limits)
    k = int(f.readline().strip().split()[0])
    pressed_seq = list(map(int, f.readline().strip().split()))

answ_array = ['NO'] * (n + 1)
for press in pressed_seq:
    if limits[press] == 0:
        answ_array[press] = 'YES'
    else:
        limits[press] -= 1

print(*answ_array[1:])

