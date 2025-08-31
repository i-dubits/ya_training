


with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))


def prefix_function(arr):
    prefix = [0] * len(arr)

    for i in range(1, len(arr)):
        border_cand = prefix[i - 1]
        while border_cand > 0 and arr[i] != arr[border_cand]:
            border_cand = prefix[border_cand - 1]

        if border_cand == 0 and arr[i] == arr[border_cand]:
            prefix[i] = 1
        elif border_cand == 0 and arr[i] != arr[border_cand]:
            prefix[i] = 0
        elif border_cand != 0 and arr[i] == arr[border_cand]:
            prefix[i] = border_cand + 1

    return prefix


# arr = [1,2,1,1]
reverse_arr = arr[::-1]
total_arr = reverse_arr + ['SEP'] + arr
# total_arr = reverse_arr + arr

prefix_total = prefix_function(total_arr)
# print(prefix_total)

suffix_palindrome_length = prefix_total[-1]
if suffix_palindrome_length >= len(arr):
    print(0)
else:
    ans = len(arr) - suffix_palindrome_length
    print(ans)
    print(*arr[:ans][::-1])







