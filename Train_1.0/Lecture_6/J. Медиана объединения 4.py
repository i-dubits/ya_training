with (open('input.txt', 'r') as f):
    N, L = map(int, f.readline().strip().split())
    seq_list = [[None for _ in range(L)] for _ in range(N)]
    dict_list = []
    for i in range(N):
        seq_list[i] = list(map(int,f.readline().strip().split()))


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
    max_ar_1, _ = search_right(arr_1, value)

    min_ar_2, in_array_2 = search_left(arr_2, value)
    max_ar_2, _ = search_right(arr_2, value)

    if in_array_1 and in_array_2:
        total_max = max_ar_1 + max_ar_2
    else:
        total_max = max_ar_1 + max_ar_2 + 1

    total_min = min_ar_1 + min_ar_2

    if desired_number_of_el >= total_min:
        return True
    else:
        return False

def binary_search(arr_1, arr_2):
    l_value = -30_001
    r_value = 30_001

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
        l_value = binary_search(seq_list[i], seq_list[j])
        print(l_value)
        #test(seq_list[i], seq_list[j])

# arr = [1, 1, 15, 18, 20, 20, 30]
# print(search_left(arr, 4))
# print(search_right(arr, 4))

# arr_1 = [4, 5]
# arr_2 = [3, 8]
# check(arr_1, arr_2, 5)




