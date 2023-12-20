#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('input.txt', 'r') as f:
    N, M = list(map(int, f.readline().strip().split()))
    arr = [[None]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        arr[i][1:] = list(map(int, f.readline().strip().split()))

dp = [[None]*(M+1) for _ in range(N+1)]
dp[0] = [0]*(M+1)
for i in range(N+1):
    dp[i][0] = 0
                
res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] != 0:
            dp[i][j] = min((dp[i-1][j], dp[i][j-1], dp[i-1][j-1])) + 1
            if dp[i][j] > res:
                res = dp[i][j]
        else:
            dp[i][j] = 0

print(res)


            