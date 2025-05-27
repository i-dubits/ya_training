with (open('input.txt', 'r') as f):
    total_people, groups_number, people_per_group = map(int, f.readline().strip().split())
    arr = [None] * total_people
    for i in range(total_people):
        arr[i] = int(f.readline().strip())


arr = sorted(arr)

def check(max_diff):
    count = 0
    i = 0
    while i <= len(arr) - people_per_group:
        diff_curr = arr[i + people_per_group - 1] - arr[i]
        if diff_curr > max_diff:
            i += 1
        else:
            count += 1
            i = i + people_per_group
        if count == groups_number:
            return True


    return False

l = 0
r = max(arr) - min(arr)

while l < r - 1:
    m = l + (r - l) // 2

    if check(m):
        r = m
    else:
        l = m

if check(l):
    print(l)
elif check(r):
    print(r)
