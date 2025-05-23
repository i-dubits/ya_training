with (open('input.txt', 'r') as f):
    height = int(f.readline())
    width = int(f.readline())
    given_area = int(f.readline())

total_area = height * width

def check(edge_thickness):
    if height < edge_thickness * 2 or width < edge_thickness * 2:
        return False, None
    else:
        void_area = (height - 2 * edge_thickness) * (width - 2 * edge_thickness)

    edge_area = total_area - void_area

    if edge_area > given_area:
        return False, edge_area
    else:
        return True, edge_area

l = 0
r = min(height, width)

while l < r - 1:
    m = l + (r - l) // 2

    if check(m)[0]:
        l = m
    else:
        r = m

if check(l)[0]:
    print(l)
else:
    print(r)