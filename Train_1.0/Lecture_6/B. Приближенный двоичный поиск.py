with (open('input.txt', 'r') as f):
    n, k = list(map(int, f.readline().strip().split()))
    arr_1 = list(map(int, f.readline().strip().split()))
    arr_2 = list(map(int, f.readline().strip().split()))


def bin_search(el):
    l = -1
    r = n

    while l < r - 1:
        m = l + (r - l) // 2
        if arr_1[m] > el:
            r = m
        else:
            l = m

    left_el, right_el = None, None
    if l != -1:
        left_el = arr_1[l]
    if r != n:
        right_el = arr_1[r]

    if left_el != None and right_el != None:
        diff_left = abs(left_el - el)
        diff_right = abs(right_el - el)
        if diff_left < diff_right:
            return left_el
        elif diff_left > diff_right:
            return right_el
        elif diff_left == diff_right:
            return min(right_el, left_el)
    elif left_el:
        return left_el
    elif right_el:
        return right_el


for el in arr_2:
    res = bin_search(el)
    print(res)