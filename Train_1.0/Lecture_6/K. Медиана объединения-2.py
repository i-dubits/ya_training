
import math
from array import array


def create_arr(x_1, d_1, a, c, m):
    seq = array('q', [0] * L)
    seq[0] = x_1
    d = d_1
    for i in range(1, L):
        seq[i] = seq[i - 1] + d
        d = (a * d + c) % m
    return seq

with (open('input.txt', 'r') as f):
    N, L = map(int, f.readline().strip().split())
    seq_list = [None for _ in range(N) ]
    for i in range(N):
        x_1, d_1, a, c, m = map(int,f.readline().strip().split())
        seq_list[i] = create_arr(x_1, d_1, a, c, m)


def search_left(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2

        if arr[m] >= value:
            r = m
        elif arr[m] < value:
            l = m

    if r != len(arr):
        if arr[r] == value:
            return r, True
        else:
            return r, False
    else:
        return len(arr), False


def search_right(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2

        if arr[m] <= value:
            l = m
        elif arr[m] > value:
            r = m

    if l != -1:
        if arr[l] == value:
            return l, True
        else:
            return l + 1, False
    else:
        return 0, False


def check(arr_1, arr_2, value):

    desired_number_of_el = len(arr_1) - 1

    min_ar_1, in_array_1 = search_left(arr_1, value)
    min_ar_2, in_array_2 = search_left(arr_2, value)
    total_min = min_ar_1 + min_ar_2

    if desired_number_of_el >= total_min:
        return True
    else:
        return False

def binary_search(arr_1, arr_2, min_value, max_value):
    l_value = min_value - 1
    r_value = max_value + 1

    while l_value < r_value - 1:
        m_value = l_value + (r_value - l_value) // 2

        if check(arr_1, arr_2, m_value):
            l_value = m_value
        else:
            r_value = m_value

    return l_value

def brute_force(arr_1, arr_2):
    res = sorted(arr_1 + arr_2)[len(arr_1) - 1]
    return res

def test(arr_1, arr_2):
    sol_ans = binary_search(arr_1, arr_2)
    correct_ans = brute_force(arr_1, arr_2)

    if sol_ans != correct_ans:
        print(f'Arr_1:\n{arr_1} ')
        print(f'Arr_2:\n{arr_2} ')
        print(f'Got: {sol_ans}')
        print(f'Expected: {correct_ans}')


for i in range(N):
    for j in range(i + 1, N):
        l_value = binary_search(seq_list[i], seq_list[j],
                                min(seq_list[i][0], seq_list[j][0]),
                                max(seq_list[i][-1], seq_list[j][-1]),
                                )
        print(l_value)
        #test(seq_list[i], seq_list[j])

# arr = [1, 1, 15, 18, 20, 20, 30]
# print(search_left(arr, 4))
# print(search_right(arr, 4))

# arr_1 = [4, 5]
# arr_2 = [3, 8]
# check(arr_1, arr_2, 5)


