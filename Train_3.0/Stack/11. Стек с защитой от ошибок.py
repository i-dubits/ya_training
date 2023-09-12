#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://contest.yandex.ru/contest/45468/problems/11/

class Stack():
    
    def __init__(self):
        self.my_stack = []
        self.if_exit = False
        
    def push(self, n):
        self.my_stack.append(n)
        return 'ok'
    
    def pop(self):
        if self.my_stack:
            return self.my_stack.pop()
        else:
            return 'error'
        
    def back(self):
        if self.my_stack:
            return self.my_stack[-1]
        else:
            return 'error'
        
    def size(self):
        return len(self.my_stack)
    
    def exit_method(self):
        self.my_stack = []
        self.if_exit = True
        return 'bye'
    
    def clear(self):
        self.my_stack = []
        return 'ok'
    
stack_inst = Stack()

with open('input.txt', 'r') as f:
   for line in f:
       
       input_string = line.split()
       if len(input_string) == 2:
           key, value = input_string[0], int(input_string[1])
       else:
           key = input_string[0]
           value = None
        
       #print(f'{key} {value}')
       
       if stack_inst.if_exit == False:
           if key == 'push':
               print(stack_inst.push(value))
           elif key == 'back':
               print(stack_inst.back())
           elif key == 'size':
               print(stack_inst.size())
           elif key == 'clear':
               print(stack_inst.clear())
           elif key == 'exit':
               print(stack_inst.exit_method())
           elif key == 'pop':
               print(stack_inst.pop())




















