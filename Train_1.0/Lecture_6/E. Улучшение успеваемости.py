with (open('input.txt', 'r') as f):
    two = int(f.readline())
    three = int(f.readline())
    four = int(f.readline())

less_than_five_sum = two * 2 + three * 3 + four * 4
less_than_five_count = two + three + four


def check(five):
    overall_sum = five * 5 + less_than_five_sum
    overall_count = less_than_five_count + five

    base = overall_sum // overall_count
    remainder = overall_sum % overall_count

    if remainder >= abs(remainder - overall_count):
        add = 1
    else:
        add = 0

    ans = base + add
    return ans >= 4, ans

l = 0
r = less_than_five_count

while l < r - 1:
    m = l + (r - l) // 2
    if check(m)[0]:
        r = m
    else:
        l = m

if check(l)[0]:
    print(l)
else:
    print(r)
