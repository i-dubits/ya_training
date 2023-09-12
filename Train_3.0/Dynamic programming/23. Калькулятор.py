#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://contest.yandex.ru/contest/45468/problems/23/

with open('input.txt', 'r') as f:
   N = int(f.readline())

dp = [0] * (N+1)
prev_numb = [0] * (N+1)

dp[0] = 0
dp[1] = 0

prev_numb[0] = 0
prev_numb[1] = 1


for i in range(2, N+1):
    
    if i%2 == 0 and i%3 == 0:
        my_dict = {'mult_2':dp[i//2] + 1, 'mult_3':dp[i//3] + 1, 'sum_1':dp[i-1] + 1}
        min_key = min( my_dict, key=my_dict.get )
        dp[i] = my_dict[min_key]
    
    elif i%2 == 0 and i%3 != 0:
        my_dict = {'mult_2':dp[i//2] + 1, 'sum_1':dp[i-1] + 1}
        min_key = min( my_dict, key=my_dict.get )
        dp[i] = my_dict[min_key]
        
    elif i%2 != 0 and i%3 == 0:
        my_dict = {'mult_3':dp[i//3] + 1, 'sum_1':dp[i-1] + 1}
        min_key = min( my_dict, key=my_dict.get )
        dp[i] = my_dict[min_key]
        
    elif i%2 != 0 and i%3 != 0:
        my_dict = {'sum_1':dp[i-1] + 1}
        min_key = min( my_dict, key=my_dict.get )
        dp[i] = my_dict[min_key]
        
    if min_key == 'mult_2':
        prev_numb[i] = i//2
        
    elif min_key == 'mult_3':
        prev_numb[i] = i//3
        
    elif min_key == 'sum_1':
        prev_numb[i] = i-1
        

answ = []

i = N
answ.append(i)
while i != 1:
    answ.append(prev_numb[i])
    i = prev_numb[i]
    
answ = answ[::-1]

print(dp[N])
print(*answ)   
