from dataclasses import dataclass, field

from collections import Counter




with (open('input.txt', 'r') as f):
    table_size, word_number = map(int, f.readline().strip().split())
    my_counter = Counter()
    for _ in range(table_size):
        row_str_list = list(f.readline().strip())
        my_counter.update(row_str_list)

    word_list = []
    for _ in range(word_number):
        row_str_list = list(f.readline().strip())
        word_list.append(row_str_list)

for word in word_list:
    curr_counter = Counter(word)
    my_counter = my_counter - curr_counter

ans = []
for letter in my_counter:
    if my_counter[letter] != 0:
        ans.append(letter*my_counter[letter])

print(''.join(ans))