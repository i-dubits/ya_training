from collections import defaultdict

with (open('input.txt', 'r') as f):
    n, k = list(map(int, f.readline().strip().split()))
    arr = list(map(int, f.readline().strip().split()))

n = len(arr)
arr = sorted(arr)
count = 0
freq_dict = defaultdict(int)


# Cardinality of the set of all values of the sliding window that appear more than once (2 or more times)
A = 0
# Cardinality of the set of all values of the sliding window that appear more than twice (3 or more times
B = 0
# Number of distinct elements in sliding windows

valid_window = False

first = 0
second = 1

def calc_count(A, B, distinct_values):
    return distinct_values * (distinct_values - 1) * (distinct_values - 2) + 3 * (distinct_values - 1) * A + B

last_valid_first = None
last_valid_second = None

freq_dict = defaultdict(int)
freq_dict[arr[first]] += 1
A = 0
B = 0
distinct_values = 1

while first < n:

    while second < n and (arr[first] * k >= arr[second] or second == first + 1):

        if last_valid_second and second - first + 1 > 2 and last_valid_second == second - 1:
            count -= calc_count(A, B, distinct_values)

        if second - first + 1 >= 3:
            valid_window = True
        if arr[second] not in freq_dict:
            distinct_values += 1

        freq_dict[arr[second]] += 1
        if freq_dict[arr[second]] == 2:
            A += 1
        if freq_dict[arr[second]] == 3:
            B += 1

        second += 1

    if valid_window:
        count += calc_count(A, B, distinct_values)
        last_valid_second = second - 1
        valid_window = False

    if second == n:
        break
    else:
        freq_dict[arr[first]] -= 1
        if freq_dict[arr[first]] == 0:
            distinct_values -= 1
        if freq_dict[arr[first]] == 1:
            A -= 1
        if freq_dict[arr[first]] == 2:
            B -= 1

        first += 1



print(count)

