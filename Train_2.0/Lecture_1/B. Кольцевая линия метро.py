with (open('input.txt', 'r') as f):
    N, i, j = map(int, f.readline().strip().split())

if i < j:
    pass
else:
    i, j = j, i

first_option = j - i - 1
second_option = i - 1 + N - j

print(min(first_option, second_option))
