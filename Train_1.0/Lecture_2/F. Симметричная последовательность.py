
#from icecream import ic

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))


def check_palindrom(arr):
    if len(arr) == 1:
        return 1

    if len(arr) % 2 == 1:
        cent_curr = len(arr) // 2
        left = cent_curr - 1
        right = cent_curr + 1
    else:
        left = len(arr) // 2 - 1
        right = len(arr) // 2

    while left >= 0 and right < len(arr):
        if arr[left] == arr[right]:
            left -= 1
            right += 1
        else:
            return False
    return True


def build_palindrom(arr, left, right):
    numbs_to_add = []
    while left >= 0:
        if right < len(arr) - 1:
            if arr[left] == arr[right]:
                left -= 1
                right += 1
            else:
                return None
        elif right == len(arr) - 1:
            if left == right - 1 and arr[left] == arr[right]:
                pass
            elif left == right - 1:
                numbs_to_add.append(arr[left])
            elif arr[left] == arr[right]:
                pass
            else:
                return None
            right += 1
            left -= 1
        elif right > len(arr) - 1:
            numbs_to_add.append(arr[left])
            right += 1
            left -= 1
    return numbs_to_add


# arr = [1,1]
# print(check_palindrom(arr))
jump_right = True
if check_palindrom(arr):
    print(0)
else:
    len_min = len(arr) * 2
    #ic(len_min)
    curr_list = []
    if len(arr) % 2 == 1:
        cent_curr = len(arr) // 2
        left = cent_curr - 1
        right = cent_curr
    else:
        left = len(arr) // 2 - 1
        right = len(arr) // 2

    #ic(left, right)
    while left < len(arr) - 1:
        res_curr = build_palindrom(arr, left, right)
        if res_curr and len_min > len(res_curr):
            curr_list = res_curr
            len_min = len(res_curr)

        if right < len(arr):
            if jump_right:
                right = right + 1
                left = left
                jump_right = not jump_right
            else:
                right = right
                left += 1
                jump_right = not jump_right
        else:
            break

    print(len_min)
    print(*curr_list)
