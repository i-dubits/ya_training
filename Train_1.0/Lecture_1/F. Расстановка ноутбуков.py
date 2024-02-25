
with open('input.txt', 'r') as f:
    x1, y1, x2, y2 = map(int, f.readline().strip().split())

def calc_area(first, second):
    return first * second

def calc_size(x1, y1, x2, y2):
    size_curr = ((y1 + y2),  max(x1, x2))
    if calc_area(*size_curr) > calc_area(x1 + x2, max(y1, y2)):
        size_curr = (x1 + x2, max(y1, y2))
    return size_curr

size_1 = calc_size(x1, y1, x2, y2)
size_2 = calc_size(y1, x1, x2, y2)
size_3 = calc_size(x1, y1, y2, x2)
size_4 = calc_size(y1, x1, y2, x2)

size_list = [size_1, size_2, size_3, size_4]
size_best = size_list[0]
size_best_area = calc_area(*size_best)

for size in size_list[1:]:
    if calc_area(*size) < size_best_area:
        size_best = size
        size_best_area = calc_area(*size_best)

print(*size_best)






