with open('input.txt', 'r') as f:
    n, m, k = map(int, f.readline().strip().split())
    mine_coord = set()
    for _ in range(k):
        y, x = map(int, f.readline().strip().split())
        mine_coord.add((y-1, x-1))

def print_array(arr):
    lines = [' '.join(map(str,line)) for line in arr]
    print('\n'.join(lines))

#arr = [[1,2,3], [5, 6, 7], [8, 9, 10]]
#print_array(arr)

X_MAX = m - 1
Y_MAX = n - 1
def check_nearest_mines(y, x, mine_coord):
    mine_count = 0

    up = (y-1, x) if y > 0 else None
    down = (y+1, x) if y < Y_MAX else None
    right = (y, x+1) if x < X_MAX else None
    left = (y, x-1) if x > 0 else None
    up_right = (y-1, x+1) if y > 0 and x < X_MAX else None
    up_left = (y-1, x-1) if y > 0 and x > 0 else None
    down_right = (y+1, x+1) if y < Y_MAX and x < X_MAX else None
    down_left = (y+1, x-1) if y < Y_MAX and x > 0 else None

    dir_list = [up, down, right, left, up_right, up_left, down_right, down_left]
    for cell in dir_list:
        if cell is not None:
            if cell in mine_coord:
                mine_count += 1

    return mine_count


def build_field(n, m, k, mine_coord):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    if k == 0:
        return arr

    for y in range(n):
        for x in range(m):
            if (y, x) in mine_coord:
                arr[y][x] = '*'
            else:
                arr[y][x] = check_nearest_mines(y, x, mine_coord)

    return arr

arr = build_field(n, m, k, mine_coord)
print_array(arr)

