
def to_bin_mask(el_list):
    bin_mask = 0
    for el in el_list:
        bin_mask |= 1 << (el - 1)

    return bin_mask


def mask_to_list(mask: int, N: int) -> list[int]:
    UNIVERSE = (1 << N) - 1
    m = mask & UNIVERSE                 # trim stray bits
    return [i + 1 for i in range(N) if (m >> i) & 1]

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())

    UNIVERSE = (1 << N) - 1
    yes_set = UNIVERSE # all elements are here in the beginning
    no_set = 0
    while True:
        curr_line = f.readline().strip()
        if curr_line[0] == 'H':
            break

        curr_list = list(map(int, curr_line.split()))
        next_line = f.readline().strip()

        if next_line[0] == 'Y':
            yes_set &= to_bin_mask(curr_list)

        elif next_line[0] == 'N':
            no_set |= to_bin_mask(curr_list)

        else:
            print(f'Something is wrong with line: {next_line}')

target = yes_set & (~no_set & UNIVERSE)
print(*sorted( mask_to_list(target, N) ) )

# print(*sorted( target ) )