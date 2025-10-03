with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())

    arr_count = [0] * (N + 1)
    arr_ban = [False] * (N + 1)

    yes_count = 0
    while True:
        curr_line = f.readline().strip()
        if curr_line[0] == 'H':
            break

        curr_list = list(map(int, curr_line.split()))
        next_line = f.readline().strip()

        if next_line[0] == 'Y':
            yes_count += 1

            for el in curr_list:
                arr_count[el] += 1

        elif next_line[0] == 'N':
            for el in curr_list:
                arr_ban[el] = True

        else:
            print(f'Something is wrong with line: {next_line}')

target = []
el = 1
for count, if_ban in zip(arr_count[1:], arr_ban[1:]):
    if count == yes_count and if_ban == False:
        target.append(el)
    el += 1

print(*sorted( target ) )