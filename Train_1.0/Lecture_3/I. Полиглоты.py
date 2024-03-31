with (open('input.txt', 'r') as f):
    N = int(f.readline().strip().split()[0])
    puple_sets = [None] * N
    intersec = set()
    union = set()
    for i in range(N):
        M = int(f.readline().strip().split()[0])
        curr_set = set()
        for _ in range(M):
            curr_language = f.readline().strip()
            curr_set.add(curr_language)

        puple_sets[i] = curr_set
        if i == 0:
            intersec = puple_sets[i]
            union = puple_sets[i]
        else:
            intersec = intersec.intersection(puple_sets[i])
            union = union.union(puple_sets[i])

print(len(intersec))
for el in intersec:
    print(el)
print(len(union))
for el in union:
    print(el)

