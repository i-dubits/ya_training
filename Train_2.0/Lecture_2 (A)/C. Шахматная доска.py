


with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr_coord = [[0 for j in range(10)] for i in range(10)]
    for i in range(N):
        x, y = map(int, f.readline().strip().split())
        arr_coord[x][y] = 1

coord_shift_x = [1, -1,  0,  0]
coord_shift_y = [0,  0,  1, -1]

def calc_length(arr_coord):
    length = 0
    for y in range(1, 9):
        for x in range(1, 9):
            for x_nei, y_nei in zip(coord_shift_x, coord_shift_y):
                if arr_coord[x][y] == 1 and arr_coord[x + x_nei][y + y_nei] == 0:
                    length += 1
                else:
                    pass

    return length

length = calc_length(arr_coord)
print(length)

