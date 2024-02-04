
with open('input.txt', 'r') as f:
    t_init, t_target = map(int, f.readline().strip().split())
    mode = f.readline().strip()

answ = None
if mode == 'heat':
    answ = max(t_init, t_target)
elif mode == 'freeze':
    answ = min(t_init, t_target)
elif mode == 'auto':
    answ = t_target
elif mode == 'fan':
    answ = t_init

print(answ)
