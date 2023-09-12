#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/23/

with open('input.txt', 'r') as f:
    N = int(f.readline())

    A = [4000]*(N+3)
    B = [4000]*(N+3)
    C = [4000]*(N+3)
    
    dp = [0]*(N+3)

    for i in range(3, N+3):
        A[i], B[i], C[i] = map(int, f.readline().strip().split(' '))
        

for i in range(3, N+3):
    
    dp[i] = min( dp[i-1] + A[i], dp[i-2] + B[i-1], dp[i-3] + C[i-2] )    
    
print(dp[-1])
    
