
from collections import defaultdict


with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().strip().split())
    source_str = f.readline().strip()
    list_of_pairs = []
    for _ in range(k):
        first, second = list(f.readline().strip())
        list_of_pairs.append((first, second))

l_to_l_freq = [[0 for k in range(26)] for i in range(26)]
l_meet_before = [0 for k in range(26)]

def proc_str(source_str):
    char_freq = [0 for i in range(26)]

    for ind in range(len(source_str) - 1, -1, -1):
        curr_char = source_str[ind]
        char_ind = ord(curr_char) - ord('a')
        if ind != len(source_str) - 1:
            if l_meet_before[char_ind] == 0:
                l_to_l_freq[char_ind] = char_freq.copy()
                l_meet_before[char_ind] = 1
            else:
                l_to_l_freq[char_ind] = list(map(lambda x, y: x + y, l_to_l_freq[char_ind], char_freq))

        char_freq[ord(curr_char) - ord('a')] += 1

    return l_to_l_freq

l_to_l_freq = proc_str(source_str)
ans = 0
for pair in list_of_pairs:
    first_ind, second_ind = ord(pair[0]) - ord('a'), ord(pair[1]) - ord('a')

    ans += l_to_l_freq[first_ind][second_ind]

print(ans)



