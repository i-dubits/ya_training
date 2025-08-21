
arr = []
with (open('input.txt', 'r') as f):
    first_el = True
    max_el = None
    while True:
        curr = int(f.readline().strip())
        if curr == 0:
            break
        else:
            if first_el:
                max_el = curr
                first_el = False
            else:
                max_el = max(curr, max_el)

            arr.append(curr)

counter = 0
for el in arr:
    if el == max_el:
        counter += 1

print(counter)
