#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def radix_sort(strings):
    max_len = len(strings[0])
    for digit in range(max_len - 1, -1, -1):
        sorted_strings = [[] for _ in range(10)]
        for string in strings:
            sorted_strings[int(string[digit])].append(string)

        print(f"**********\nPhase {max_len - digit}")
        for i, bucket in enumerate(sorted_strings):
            print(f"Bucket {i}: {'empty' if not bucket else ', '.join(bucket)}")

        strings = [string for bucket in sorted_strings for string in bucket]

    return strings

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    input_strings = [None]*N
    for i in range(N):
        #curr =  f.readline().strip()
        input_strings[i] = f.readline().strip()
    

print("Initial array:\n" + ", ".join(input_strings))

sorted_array = radix_sort(input_strings)

print("**********\nSorted array:\n" + ", ".join(sorted_array))






