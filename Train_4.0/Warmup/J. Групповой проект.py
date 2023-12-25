#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check(n, a, b):
    groups = n // a
    remain = n % a
    
    if remain <= groups * (b - a):
        print('YES')
    else:
        print('NO')

with open('input.txt', 'r') as f:
   t = int(f.readline().strip())
   for i in range(t):
       n, a, b = list(map(int, f.readline().strip().split()))
       check(n, a, b)
















