with (open('input.txt', 'r') as f):
    n = int(f.readline().strip().split()[0])
    a_to_b = {}
    b_to_a = {}

    for i in range(n):
        a, b = f.readline().strip().split()
        a_to_b[a] = b
        b_to_a[b] = a
    target = f.readline().strip().split()[0]

    if target in a_to_b:
        print(a_to_b[target])
    elif target in b_to_a:
        print(b_to_a[target])



