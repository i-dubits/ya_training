with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))

print(len(set(arr)))