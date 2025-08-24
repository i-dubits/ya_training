

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))
    M = int(f.readline().strip())
    requests = list(map(int, f.readline().strip().split()))

def right_search(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2

        if arr[m] <= value:
            l = m
        else:
            r = m

    if l < len(arr) and arr[l] == value:
        return l + 1
    else:
        return 0


def left_search(arr, value):
    l = -1
    r = len(arr)

    while l < r - 1:
        m = l + (r - l) // 2

        if arr[m] < value:
            l = m
        else:
            r = m

    if r < len(arr) and arr[r] == value:
        return r + 1
    else:
        return 0


for value in requests:
    right = right_search(arr, value)
    left = left_search(arr, value)

    print(f'{left} {right}')