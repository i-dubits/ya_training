
with (open('input.txt', 'r') as f):
    init_str = f.readline().strip()

ans = 0

def number_of_changes(init_str):

    if len(init_str) == 1:
        return 0

    ans = 0
    i = 0
    j = len(init_str) - 1

    while i < j:
        if init_str[i] != init_str[j]:
           ans += 1

        i += 1
        j -= 1

    return ans

print(number_of_changes(init_str))