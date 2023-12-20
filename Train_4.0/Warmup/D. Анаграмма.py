#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

with open('input.txt', 'r') as f:
    str_1 = f.readline().strip()
    str_2 = f.readline().strip()

cnt_1 = Counter(str_1)
cnt_2 = Counter(str_2)

if cnt_1 == cnt_2:
    print('YES')
else:
    print('NO')






