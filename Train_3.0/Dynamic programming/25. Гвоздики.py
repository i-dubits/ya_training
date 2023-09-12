#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/25/

from IPython.core.debugger import set_trace

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())

    coords = [-1] * N

    coords = list(map(int, f.readline().strip().split()))
        
dp = [15_000]*N

coords = sorted(coords)

coord_diff = [coords[i] - coords[i-1] for i in range(1, N)]

dp[1] = coord_diff[0]

if N > 2:
    for i in range(2, N):
        #set_trace()
        dp[i] =  min(dp[i-1], dp[i-2]) + coord_diff[i-1]
                
print(dp[-1])
       

    
