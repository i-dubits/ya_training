

with (open('input.txt', 'r') as f):
    code_pr = int(f.readline().strip())
    code_inter = int(f.readline().strip())
    code_checker = int(f.readline().strip())


ans = code_inter
if code_inter == 0:
    if code_pr != 0:
        ans = 3
    else:
        ans = code_checker

elif code_inter == 1:
    ans = code_checker

elif code_inter == 4:
    if code_pr != 0:
        ans = 3
    else:
        ans = 4

elif code_inter == 6:
    ans = 0

elif code_inter == 7:
    ans = 1

print(ans)


