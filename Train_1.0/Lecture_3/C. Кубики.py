with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().strip().split())
    first = set()
    second = set()
    for _ in range(n):
        first.add(int(f.readline().strip().split()[0]))
    for _ in range(m):
        second.add(int(f.readline().strip().split()[0]))

intersec = first.intersection(second)
first_only = first.difference(intersec)
second_only = second.difference(intersec)

print(len(intersec))
print(*sorted(list(intersec)))
print(len(first_only))
print(*sorted(list(first_only)))
print(len(second_only))
print(*sorted(list(second_only)))
