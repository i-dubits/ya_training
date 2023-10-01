#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/19/


class Heap():
    def __init__(self):
        self.arr = [None] * 100000
        self.pos_last = 0
    
    def insert(self, value):
        self.arr[self.pos_last] = value
        self.shift_up(self.pos_last)
        self.pos_last += 1
        
    def shift_up(self, pos):
        while pos > 0 and self.arr[(pos-1)//2] < self.arr[pos]:
            self.arr[(pos-1)//2], self.arr[pos] = self.arr[pos], self.arr[(pos-1)//2]
            pos = (pos-1)//2
            
    def extract(self):
        max_val = self.arr[0]
        self.arr[0] = self.arr[self.pos_last-1]
        self.shift_down(0)
        return max_val
        
    def shift_down(self, pos):
        left = pos*2 + 1
        right = pos*2 + 2        
        while left < self.pos_last-1:
            pos_max = left if self.arr[left] > self.arr[right] else right
            if self.arr[pos_max] > self.arr[pos]:
                self.arr[pos_max], self.arr[pos] = self.arr[pos], self.arr[pos_max]
                pos = pos_max
                left = pos*2 + 1
                right = pos*2 + 2
            else:
                break
            
        self.pos_last -= 1

heap_inst = Heap()

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    for i in range(N):
        line = f.readline().strip().split()
        if len(line) == 2:
            value = int(line[1])
            heap_inst.insert(value)
            #print(value)
            #print(line)
            #print(f'Add: {value}, result array: {heap_inst.arr}')
            if value == 365:
                pass
        elif len(line) == 1:
            max_val = heap_inst.extract()
            print(max_val)
            #print(f'After {max_val} removal: {heap_inst.arr}')
        
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               