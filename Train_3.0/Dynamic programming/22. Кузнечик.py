#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/22/

with open('input.txt', 'r') as f:
   N, k = map(int, f.readline().split())

  
if k < N:
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(2, k+1):
        dp[i] = sum(dp[:i])
        
    for i in range(k+1, N+1):
        dp[i] = sum(dp[i-k:i])
        
    print(dp[-1])
        
else:
    dp = [0] * (k+1)
    dp[1] = 1
    for i in range(2, k+1):
        dp[i] = sum(dp[:i])
    print(dp[N])
        

    
    
    
