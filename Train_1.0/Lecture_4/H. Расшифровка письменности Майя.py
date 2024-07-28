from copy import copy
from collections import Counter

with (open('input.txt', 'r') as f):
    len_w, len_s = list(map(int, f.readline().strip().split()))
    word = f.readline().strip().split()[0]
    init_str = f.readline().strip().split()[0]

count_word_init = {}
word_sum = 0
for i in range(len(word)):
    if word[i] in count_word_init:
        count_word_init[word[i]] += 1
        word_sum += 1
    else:
        count_word_init[word[i]] = 1
        word_sum += 1

count_word_curr = copy(count_word_init)
curr_sum = word_sum


if len(init_str) == len(word):
    word_cnt = Counter(word)
    str_cnt = Counter(init_str)
    if word_cnt == str_cnt:
        print(1)
    else:
        print(0)

def sum_abs(my_dict):
    vals = my_dict.values()
    return sum(abs(val) for val in vals)

count_times = 0
process_chars_fom_restart = 0
for i in range(len(init_str)):
    # print(f'Current char: {init_str[i]}')
    if init_str[i] in count_word_curr:
        process_chars_fom_restart += 1
        old_val = count_word_curr[init_str[i]]
        count_word_curr[init_str[i]] -= 1
        if abs(old_val) < abs(count_word_curr[init_str[i]]):
            curr_sum += 1
        else:
            curr_sum -= 1
        if process_chars_fom_restart > len(word):
            if init_str[i - len(word)] in count_word_curr:
                old_val = count_word_curr[init_str[i - len(word)]]
                count_word_curr[init_str[i - len(word)]] += 1
                if abs(old_val) < abs(count_word_curr[init_str[i - len(word)]]):
                    curr_sum += 1
                else:
                    curr_sum -= 1

        if curr_sum == 0:
            # print(f'{init_str[i - len(word) + 1:i+1]}')
            count_times += 1
    else:
        count_word_curr = copy(count_word_init)
        curr_sum = word_sum
        process_chars_fom_restart = 0

print(count_times)
# sum_abs(count_word_curr)
