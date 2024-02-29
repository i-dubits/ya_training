with open('input.txt', 'r') as f:
    n = int(f.readline().strip().split()[0])
    voice_cond_list = []
    for i in range(n):
        if i == 0:
            curr = float(f.readline().strip().split()[0])
            voice_cond_list.append((curr, None))
        else:
            curr, cond = f.readline().strip().split()
            curr = float(curr)
            voice_cond_list.append((curr, cond))

first = voice_cond_list[0][0]
borders_x_less_than = [4000]
borders_x_more_than = [30]

for i in range(1, len(voice_cond_list)):
    second, cond = voice_cond_list[i]
    if cond == 'closer':
        average = (first + second) / 2
        if second >= first:
            borders_x_more_than.append(average)
        else:
            borders_x_less_than.append(average)
    elif cond == 'further':
        average = (first + second) / 2
        if second <= first:
            borders_x_more_than.append(average)
        else:
            borders_x_less_than.append(average)

    first = second

min_b = min(borders_x_less_than)
max_b = max(borders_x_more_than)
print(*(sorted([min_b, max_b])))