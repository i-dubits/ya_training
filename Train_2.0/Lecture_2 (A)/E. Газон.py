
import math

with (open('input.txt', 'r') as f):
    x_1, y_1, x_2, y_2 = map(int, f.readline().strip().split())
    x_3, y_3, r = map(int, f.readline().strip().split())

def x_range(r_minus_curr_y, circle_x, radius):
    max_x_centered = int(math.sqrt( r_minus_curr_y * (2 * radius - r_minus_curr_y) ) )
    min_x_centered = -max_x_centered

    max_x = max_x_centered + circle_x
    min_x = min_x_centered + circle_x

    return min_x, max_x

def find_intersection(x_1, y_1, x_2, y_2, circle_x, circle_y, radius):

    ans = 0
    for curr_y_centered in range(radius, -(radius + 1), -1):
        r_minus_curr_y = radius - abs(curr_y_centered)
        min_circle_x, max_circle_x = x_range(r_minus_curr_y, circle_x, radius)

        curr_y = curr_y_centered + circle_y
        if y_1 <= curr_y <= y_2:
            l_point_x = max(x_1, min_circle_x)
            r_point_x = min(x_2, max_circle_x)
            if l_point_x <= r_point_x:
                ans += r_point_x - l_point_x + 1

    return ans

ans = find_intersection(x_1, y_1, x_2, y_2, x_3, y_3, r)
print(ans)
