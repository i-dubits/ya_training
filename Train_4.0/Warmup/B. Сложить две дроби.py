#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('input.txt', 'r') as f:
    a, b, c, d = list(map(int, f.readline().strip().split()))

numer = a * d + b * c
den = b * d

def gcd(a, b):
    
    if a > b:
        b, a = a, b 
    while a % b != 0:
        rem = a % b
        a = b
        b = rem

    return b

gcd_val = gcd(numer, den)

print(numer//gcd_val, den//gcd_val)
            