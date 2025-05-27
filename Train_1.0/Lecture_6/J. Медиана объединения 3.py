
with (open('input.txt', 'r') as f):
    N, L = map(int, f.readline().strip().split())
    seq_list = [[None for _ in range(L)] for _ in range(N)]
    dict_list = []
    for i in range(N):
        seq_list[i] = list(map(int,f.readline().strip().split()))


def number_of_els_before_value_left_search(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2
        if arr[m] >= value:
            r = m
        else:
            l = m

    if r != len(arr):
        if arr[r] == value:
            return r, True
        else:
            return r, False
    else:
        return len(arr), False


def number_of_els_before_value_right_search(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2
        if arr[m] <= value:
            l = m
        else:
            r = m

    if l != -1:
        if arr[l] == value:
            return l, True
        else:
            return r, False
    else:
        return 0, False




def check(arr_primary, arr_second, index):
    value = arr_primary[index]

    arr_primary_before_count_left, _ = number_of_els_before_value_left_search(arr_primary, value)
    arr_primary_before_count_right, _ = number_of_els_before_value_right_search(arr_primary, value)

    arr_second_before_count_left, in_array = number_of_els_before_value_left_search(arr_second, value)
    arr_second_before_count_right, in_array = number_of_els_before_value_right_search(arr_second, value)

    min_count = arr_primary_before_count_left + arr_second_before_count_left
    max_count = arr_primary_before_count_right + arr_second_before_count_right

    if in_array is True:
        max_count += 1

    if min_count >= len(seq_list[0]) - 1:
        return True, min_count, max_count
    else:
        return False, min_count, max_count

def binary_search(arr_primary, arr_second):
    first = -1
    second = len(seq_list[0])

    while first < second - 1:
        m = first + (second - first) // 2
        if check(arr_primary, arr_second, m)[0]:
            second = m
        else:
            first = m

    if first != -1:
        _, min_count_1, max_count_1 = check(arr_primary, arr_second, first)
        if min_count_1 <= len(seq_list[0]) - 1 <= max_count_1:
            return arr_primary[first]
    if second != len(seq_list[0]):
        _, min_count_2, max_count_2 = check(arr_primary, arr_second, second)
        if min_count_2 <= len(seq_list[0]) - 1 <= max_count_2:
            return arr_primary[second]

    return None


for i in range(N):
    for j in range(i + 1, N):
        cand_1 = binary_search(seq_list[i], seq_list[j])
        cand_2 = binary_search(seq_list[j], seq_list[i])
        if cand_1 is not None:
            print(cand_1)
        elif cand_2 is not None:
            print(cand_2)
        else:
            print('ERROR!')


def check_for_indices(i, j):
    print(f'Seq_i: {seq_list[i]}')
    print(f'Seq_j: {seq_list[j]}')

    cand_1 = binary_search(seq_list[i], seq_list[j])
    cand_2 = binary_search(seq_list[j], seq_list[i])

    print(f'Cand_1: {cand_1}')
    print(f'Cand_2: {cand_2}')

    if cand_1 is not None:
        print(cand_1)
    elif cand_2 is not None:
        print(cand_2)
    else:
        print('ERROR!')


# arr_1 = [3, 8]; arr_2 = [3, 5]
# print(binary_search(arr_1, arr_2))



# arr = [1, 1, 2, 3]
# number_of_els_before_value_left_search(arr, 1)
