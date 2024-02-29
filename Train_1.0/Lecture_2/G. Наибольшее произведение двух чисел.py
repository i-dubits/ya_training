with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))


def get_max_1_2(arr):
    max_1, max_2 = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    for i in range(2, len(arr)):
        if arr[i] > max_1:
            max_2 = max_1
            max_1 = arr[i]
        elif arr[i] > max_2:
            max_2 = arr[i]

    return max_1, max_2


def get_min_1_2(arr):
    min_1, min_2 = (arr[1], arr[0]) if arr[0] > arr[1] else (arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] < min_1:
            min_2 = min_1
            min_1 = arr[i]
        elif arr[i] < min_2:
            min_2 = arr[i]

    return min_1, min_2


def get_max_product(arr):

    if len(arr) == 2:
        return sorted(arr)

    max_1, max_2 = get_max_1_2(arr)
    min_1, min_2 = get_min_1_2(arr)

    opt_1 = max_1 * max_2
    opt_2 = max_1 * min_2
    opt_3 = min_1 * min_2
    opt_4 = min_1 * max_2

    opt_dict = {max_1 * max_2: (max_1, max_2),
                max_1 * min_2: (max_1, min_2),
                min_1 * min_2: (min_1, min_2),
                min_1 * max_2: (min_1, max_2)}

    max_val = max(opt_dict)

    return sorted(opt_dict[max_val])


print(*get_max_product(arr))
