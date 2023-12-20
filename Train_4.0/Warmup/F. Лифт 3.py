#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('input.txt', 'r') as f:
    k = int(f.readline().strip())
    n = int(f.readline().strip())
    floors = [None]*(n+1)
    for i in range(n):
        floors[i+1] = int(f.readline().strip())

total_time = 0
people_numb = 0
highest_floor = n
last_floor = -1

while highest_floor >= 1:
    if floors[highest_floor] == 0:
        highest_floor -= 1
        continue

    if floors[highest_floor] % k != 0:
        last_people_numb = floors[highest_floor] % k
        numb_times = floors[highest_floor] // k + 1
        total_time += numb_times * highest_floor * 2
        
        highest_floor -= 1
        while highest_floor > 0:
            if floors[highest_floor] == 0:
                highest_floor -= 1
                continue
            elif floors[highest_floor] > k - last_people_numb:
                floors[highest_floor] = floors[highest_floor] - (k - last_people_numb)
                break
            elif floors[highest_floor] <= k - last_people_numb:
                last_people_numb += floors[highest_floor]
                highest_floor -= 1
    else:
        numb_times = floors[highest_floor] // k
        total_time += numb_times * highest_floor * 2
        last_people_numb = 0
        highest_floor -= 1
                
            
print(total_time)


            