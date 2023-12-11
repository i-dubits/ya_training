#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    s = f.readline().strip()
    
def maximal_prefix_suffix_match(s):
    p = 10 ** 9 + 7  
    x_ = 257  
    k = len(s)
    h = [0] * (k + 1) 
    x = [1] * (k + 1)  

    if len(set(s)) == 1:
        return 1

    for i in range(1, k + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i - 1])) % p
        x[i] = (x[i - 1] * x_) % p

    for l in range(k - 1, 0, -1):
        prefix_hash = h[l]
        suffix_hash = (h[k] - h[k - l] * x[l]) % p
        if prefix_hash == suffix_hash:
            return k - l

    return k

print(maximal_prefix_suffix_match(s))  