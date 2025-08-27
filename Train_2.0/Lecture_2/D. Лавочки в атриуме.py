
with (open('input.txt', 'r') as f):
    L, K = map(int, f.readline().strip().split())
    arr = list(map(int, f.readline().strip().split()))

arr_l = [0] * 10_000

for el in arr:
    arr_l[el] = 1


def go_left(arr_l, start):
    left_block_coord = None
    # move left from start
    for coord in range(start - 1, -1, -1):
        if arr_l[coord] == 1:
            left_block_coord = coord
            break

    return left_block_coord


def go_right(arr_l, start):
    right_block_coord = None
    # move left from start
    for coord in range(start + 1, len(arr_l), 1):
        if arr_l[coord] == 1:
            right_block_coord = coord
            break

    return right_block_coord

def find_blocks(arr_l, L):
    center_left = L//2
    not_edge_case = L % 2

    if arr_l[center_left] == 1:
        if not_edge_case:
            return tuple((center_left,))
        else:
            left_block = go_left(arr_l, center_left)
            return left_block, center_left

    left_block = go_left(arr_l, center_left)
    right_block = go_right(arr_l, center_left)

    return left_block, right_block

res = find_blocks(arr_l, L)

if len(res) == 1:
    print(res[0])
else:
    print(res[0], res[1])

