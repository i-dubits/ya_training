
from itertools import permutations
import os

def generate_permutations(N):
    return [''.join(map(str, perm)) for perm in sorted(permutations(range(1, N + 1)))]

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())

# Example usage with a hypothetical 'input.txt' file
for perm in sorted(permutations(range(1, N + 1))):
    print(''.join(map(str, perm)))
