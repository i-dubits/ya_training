
with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

def find_el(arr):
    max_v = max(arr)
    rest_el_sum = sum(arr) - max_v
    cand_1 = max_v - rest_el_sum

    cand_2 = sum(arr)

    if cand_1 <= 0:
        return cand_2
    elif cand_1 < cand_2:
        return cand_1
    elif cand_1 >= cand_2:
        return cand_2

res = find_el(arr)
print(res)
