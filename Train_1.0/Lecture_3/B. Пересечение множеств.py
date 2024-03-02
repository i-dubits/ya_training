with open('input.txt', 'r') as f:
    arr_1 = list(map(int, f.readline().strip().split()))
    arr_2 = list(map(int, f.readline().strip().split()))

print( *sorted(list(set(arr_1).intersection(set(arr_2)))) )