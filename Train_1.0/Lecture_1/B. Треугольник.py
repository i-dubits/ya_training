
with open('input.txt', 'r') as f:
    a = int(f.readline().strip())
    b = int(f.readline().strip())
    c = int(f.readline().strip())

if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')
