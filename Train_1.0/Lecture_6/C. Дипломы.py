with (open('input.txt', 'r') as f):
    w, h, n = list(map(int, f.readline().strip().split()))


def check(length):
    if (length // w) * (length // h) >= n:
        return True
    else:
        return False

l = 1
r = max(w, h) * n

while l < r - 1:
    m = l + (r - l) // 2
    if check(m):
        r = m
    else:
        l = m

if check(r) and check(l):
    print(l)
elif check(r):
    print(r)
elif check(l):
    print(l)