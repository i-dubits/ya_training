import math

with open('input.txt', 'r') as f:
    t, d, n = list(map(int, f.readline().strip().split()))
    signal_list = []
    for _ in range(n):
        x, y = list(map(int, f.readline().strip().split()))
        signal_list.append((x, y))


class Square:

    eps = 1e-6

    def __init__(self, x_centr, y_centr, d):

        x_up, y_up = x_centr, y_centr + d
        x_down, y_down = x_centr, y_centr - d
        x_right, y_right = x_centr + d, y_centr
        x_left, y_left = x_centr - d, y_centr

        self.a_max = max(y_down - x_down, y_up - x_up)
        self.a_min = min(y_down - x_down, y_up - x_up)
        self.b_min = min(y_down + x_down, y_up + x_up)
        self.b_max = max(y_down + x_down, y_up + x_up)

    @classmethod
    def square_from_coeff(cls, a_min, a_max, b_min, b_max):
        init_sq = cls(0, 0, 1)
        init_sq.a_min = a_min
        init_sq.a_max = a_max
        init_sq.b_min = b_min
        init_sq.b_max = b_max

        return init_sq

    @staticmethod
    def intersect_squares(sq_1: 'Square', sq_2: 'Square'):

        a_min = max(sq_1.a_min, sq_2.a_min)
        a_max = min(sq_1.a_max, sq_2.a_max)
        b_max = min(sq_1.b_max, sq_2.b_max)
        b_min = max(sq_1.b_min, sq_2.b_min)

        return Square.square_from_coeff(a_min, a_max, b_min, b_max)

    @staticmethod
    def increase_square(sq: 'Square', t: int):
        a_min = sq.a_min - t
        b_min = sq.b_min - t
        a_max = sq.a_max + t
        b_max = sq.b_max + t

        return Square.square_from_coeff(a_min, a_max, b_min, b_max)

    def get_points(self):

        points_coord = set()

        for i in range( self.a_min, self.a_max + 1 ):
            for j in range( self.b_min, self.b_max + 1 ):
                if (j-i)%2 == 0 and (i+j)%2 == 0:
                    points_coord.add( ( (j-i)//2, (i+j)//2 ) )

        return points_coord


curr_square = Square(0, 0, t)
for curr_signal in range(0, n):
    signal_square = Square(signal_list[curr_signal][0], signal_list[curr_signal][1], d)
    curr_square = Square.intersect_squares(curr_square, signal_square)

    if curr_signal != n - 1:
        curr_square = Square.increase_square(curr_square, t)

init_points = curr_square.get_points()

print(len(init_points))
for point in init_points:
    print(point[0], point[1])