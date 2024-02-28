with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))

def if_grow(arr):
    if len(arr) == 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False

    return True

print('YES') if if_grow(arr) else print('NO')