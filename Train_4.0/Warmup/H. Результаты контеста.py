#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('input.txt', 'r') as f:
    a = int(f.readline().strip())
    b = int(f.readline().strip())
    n = int(f.readline().strip())

max_st_a = a
min_st_a = a//n if a % n == 0 else a//n + 1

max_st_b = b
min_st_b = b//n if b % n == 0 else b//n + 1

if min_st_b >= max_st_a:
    print('NO')
else:
    print('YES')