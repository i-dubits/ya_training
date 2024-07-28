a = 1
from copy import copy
from collections import Counter

with (open('input.txt', 'r') as f):
    len_w, len_s = list(map(int, f.readline().strip().split()))
    word = f.readline().strip().split()[0]
    str_init = f.readline().strip().split()[0]

def count_chars(input_str):
    count_word = {}
    word_sum = 0
    for i in range(len(input_str)):
        if input_str[i] in count_word:
            count_word[input_str[i]] += 1
            word_sum += 1
        else:
            count_word[input_str[i]] = 1
            word_sum += 1
    return count_word, word_sum

true_counter, _ = count_chars(word)

if len(str_init) == len(word):
    word_cnt = Counter(word)
    str_cnt = Counter(str_init)
    if word_cnt == str_cnt:
        print(1)
    else:
        print(0)


count = 0
for i in range(len(str_init)):
    end = i + len(word)
    if end <= len(str_init):
        str_slice = str_init[i:end]
        curr_counter, _ = count_chars(str_slice)
        if true_counter == curr_counter:
            print(str_slice)
            count += 1

print(count)