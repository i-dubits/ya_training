with open('input.txt', 'r') as f:
    x, y, z = list(map(int, f.readline().strip().split()))
    target = f.readline().strip()

tg_set = set(target)

count = 0
for el in tg_set:
    if int(el) in (x,y,z):
        pass
    else:
        count += 1

print(count)