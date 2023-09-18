#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/16/


Q_SIZE = 1_000_000

class Queue():
    
    def __init__(self):
        self.my_queue = [None]*Q_SIZE
        self.head = 0
        self.tail = 0
        self.if_exit = False
        
    def push(self, n):
        self.my_queue[self.tail % Q_SIZE] = n
        self.tail += 1
        return 'ok'
    
    def pop(self):
        if self.tail - self.head > 0:
            el = self.my_queue[self.head % Q_SIZE]
            self.head += 1
            return el
        else:
            return 'error'
        
    def front(self):
        if self.tail - self.head > 0:
            return self.my_queue[self.head % Q_SIZE]
        else:
            return 'error'
        
    def size(self):
        return self.tail - self.head
    
    def exit_method(self):
        self.head = 0
        self.tail = 0
        self.if_exit = True
        return 'bye'
    
    def clear(self):
        self.head = 0
        self.tail = 0
        return 'ok'
    
queue_inst = Queue()

with open('input.txt', 'r') as f:
   for line in f:
       
       input_string = line.split()
       if len(input_string) == 2:
           key, value = input_string[0], int(input_string[1])
       elif input_string:
           key = input_string[0]
           value = None
        
       #print(f'{key} {value}')
       
       if queue_inst.if_exit == False:
           if key == 'push':
               print(queue_inst.push(value))
           elif key == 'front':
               print(queue_inst.front())
           elif key == 'size':
               print(queue_inst.size())
           elif key == 'clear':
               print(queue_inst.clear())
           elif key == 'exit':
               print(queue_inst.exit_method())
           elif key == 'pop':
               print(queue_inst.pop())
