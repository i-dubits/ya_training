
with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))

def find_min_max(arr):
    max_1, max_2, max_3 = sorted(arr[:3])
    min_1, min_2 = sorted(arr[:2])

    for i in range(3, len(arr)):
        if arr[i] >= max_3:
            max_1 = max_2
            max_2 = max_3
            max_3 = arr[i]
        elif arr[i] < max_3 and arr[i] >= max_2:
            max_1 = max_2
            max_2 = arr[i]
        elif arr[i] < max_2 and arr[i] >= max_1:
            max_1 = arr[i]

    for i in range(2, len(arr)):
        if arr[i] <= min_1:
            min_2 = min_1
            min_1 = arr[i]
        elif arr[i] > min_1 and arr[i]  <= min_2:
            min_2 = arr[i]

    return max_1, max_2, max_3, min_1, min_2

if len(arr) == 3:
    print(*arr)
else:
    max_1, max_2, max_3, min_1, min_2 = find_min_max(arr)
    max_val = max_1 * max_2 * max_3
    if max_val < min_1 * min_2 * max_3:
        print(*[min_1, min_2, max_3])
    else:
        print(*[max_1, max_2, max_3])