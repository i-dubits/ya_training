#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    s = f.readline().strip()
    Q = int(f.readline().strip())
    
    p = 10 ** 9 + 7  
    x_ = 257  
    k = len(s)
    h = [0] * (k + 1)  
    x = [1] * (k + 1)  

    for i in range(1, k + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i - 1])) % p
        x[i] = (x[i - 1] * x_) % p    
      
    for _ in range(Q):
        l, a, b = list(map(int, f.readline().strip().split()))
        hash1 = (h[a + l] - h[a] * x[l]) % p
        hash2 = (h[b + l] - h[b] * x[l]) % p
        if hash1 == hash2:
            print('yes')
        else:
            print('no')
    







