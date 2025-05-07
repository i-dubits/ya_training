with (open('input.txt', 'r') as f):
    k = int(f.readline())
    arr = f.readline().strip().split()[0]

n = len(arr)

first = 0
second = first + k

begin_window = None
valid_window = False
ans = 0


while first < n:
    while second < n and arr[first] == arr[second]:
        if not valid_window:
            begin_window = first
            valid_window = True

        win_length = second - begin_window + 1

        first += 1
        second += 1

    if valid_window:
        ans += (win_length - k) * (win_length - k + 1) // 2
        begin_window = None
        valid_window = False

    if second == n:
        break

    first += 1
    second = first + k

print(ans)

