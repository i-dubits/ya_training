
import math

with open('input.txt', 'r') as f:
    a = int(f.readline().strip())
    b = int(f.readline().strip())
    c = int(f.readline().strip())

def solution(a, b, c):
    if a == 0:
        if b < 0:
            print('NO SOLUTION')
            return
        else:
            if math.sqrt(b) == c:
                print('MANY SOLUTIONS')
                return
            else:
                print('NO SOLUTION')
    else:
        if c < 0:
            print('NO SOLUTION')
            return
        else:
            if (c*c - b) % a == 0:
                x_cand = (c*c - b) // a
            else:
                print('NO SOLUTION')
                return
            if x_cand * a + b >= 0:
                print(x_cand)
                return
            else:
                print('NO SOLUTION')
                return

solution(a, b, c)
