#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/18/

Q_SIZE = 1_000_000

class DeQueue():
    
    def __init__(self):
        self.my_queue = [None]*Q_SIZE
        self.head = 0
        self.tail = 0
        self.if_exit = False
        
    def push_back(self, n):
        self.my_queue[self.tail % Q_SIZE] = n
        self.tail += 1
        return 'ok'
    
    def push_front(self, n):
        self.head -= 1
        if self.head < 0:
            self.my_queue[self.head % Q_SIZE] = n
        else:
            self.my_queue[self.head % Q_SIZE] = n
        return 'ok'
    
    def pop_front(self):
        if self.tail - self.head > 0:
            el = self.my_queue[self.head % Q_SIZE]
            self.head += 1
            return el
        else:
            return 'error'

    def pop_back(self):
        if self.tail - self.head > 0:
            el = self.my_queue[(self.tail-1) % Q_SIZE]
            self.tail -= 1
            return el
        else:
            return 'error'
        
    def front(self):
        if self.tail - self.head > 0:
            return self.my_queue[self.head % Q_SIZE]
        else:
            return 'error'
        
    def back(self):
        if self.tail - self.head > 0:
            return self.my_queue[(self.tail - 1) % Q_SIZE]
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
    
queue_inst = DeQueue()

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
           if key == 'push_front':
               print(queue_inst.push_front(value))
           elif key == 'push_back':
               print(queue_inst.push_back(value))
           elif key == 'pop_front':
               print(queue_inst.pop_front())
           elif key == 'pop_back':
               print(queue_inst.pop_back())
           elif key == 'front':
               print(queue_inst.front())
           elif key == 'back':
               print(queue_inst.back())
           elif key == 'size':
               print(queue_inst.size())
           elif key == 'clear':
               print(queue_inst.clear())
           elif key == 'exit':
               print(queue_inst.exit_method())
           elif key == 'pop':
               print(queue_inst.pop())
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               