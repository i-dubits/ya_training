with (open('input.txt', 'r') as f):
    n, a, b, w, h = list(map(int, f.readline().strip().split()))


def check(thickness):
    new_a, new_b = a + 2 * thickness, b + 2 * thickness

    # Option 1
    count_1 = (w // new_a) * (h // new_b)
    # Option 2
    count_2 = (w // new_b) * (h // new_a)

    count = max(count_1, count_2)
    if count >= n:
        return True
    else:
        return False


l = 0
r = max(w, h)

while l < r - 1:
    m = l + (r - l) // 2

    if check(m):
        l = m
    else:
        r = m

ans_cand_1 = None
ans_cand_2 = None

if check(l) and l != 0:
    ans_cand_1 = l
elif check(r) and r != 0:
    ans_cand_2 = r

if ans_cand_1 is not None and ans_cand_2 is not None:
    ans = max(ans_cand_1, ans_cand_2)
elif ans_cand_1:
    ans = ans_cand_1
elif ans_cand_2:
    ans = ans_cand_2
else:
    ans = 0

print(ans)
