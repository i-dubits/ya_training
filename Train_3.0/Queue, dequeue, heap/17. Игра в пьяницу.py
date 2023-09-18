#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/17/

from collections import deque


with open('input.txt', 'r') as f:
       first = list(map(int, f.readline().strip().split()))
       second = list(map(int, f.readline().strip().split()))


first_q = deque(first)
second_q = deque(second)

count = 0

while True:
    
    if count < 1_000_000:
        
        if not first_q:
            print(f'second {count}')
            break
        if not second_q:
            print(f'first {count}')
            break
        
        count+=1
        first_curr = first_q.popleft()
        second_curr = second_q.popleft()
        
        if first_curr == 0 and second_curr == 9:
            first_q.append(first_curr)
            first_q.append(second_curr)
        elif first_curr == 9 and second_curr == 0:
            second_q.append(first_curr)
            second_q.append(second_curr)
        else:
            if first_curr > second_curr:
                first_q.append(first_curr)
                first_q.append(second_curr)
            else:
                second_q.append(first_curr)
                second_q.append(second_curr)       

        
    else:
        print('botva')
        break
    