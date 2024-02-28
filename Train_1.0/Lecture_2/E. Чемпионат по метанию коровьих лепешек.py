with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

def find_vas_position(arr):
    first_max_ind = 0
    first_max_value = arr[first_max_ind]
    for i in range(1, len(arr)):
        if first_max_value < arr[i]:
            first_max_value = arr[i]
            first_max_ind = i

    vas_ind = []
    vas_value = -1
    for i in range(first_max_ind + 1, len(arr) - 1):
        if arr[i] % 10 == 5 and arr[i] > arr[i+1] and arr[i] > vas_value:
            vas_value = arr[i]
            vas_ind = i

    if vas_value == -1:
        return 0

    count_more_then = 0
    for i in range(len(arr)):
        if arr[i] > vas_value:
            count_more_then += 1

    return count_more_then + 1

vas_pos = find_vas_position(arr)
print(vas_pos)