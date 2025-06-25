

BLOCK_START = 1
BLOCK_END = 0

with (open('input.txt', 'r') as f):

    N, W, L = map(int, f.readline().strip().split())

    events = []
    for index in range(N):
        x_1, y_1, z_1, x_2, y_2, z_2 = map(int, f.readline().strip().split())
        area = (y_2 - y_1) * (x_2 - x_1)

        events.append( (z_1, BLOCK_START, area, index) )    # z-coord, type, area, index
        events.append( (z_2, BLOCK_END, area, index) )



min_block_number = N + 1
current_area = 0
target_area = W * L
active_blocks_set = set()


events.sort()
for ev in events:

    z_coord = ev[0]
    block_type = ev[1]
    block_area = ev[2]
    index = ev[3]

    if block_type == BLOCK_START:
        active_blocks_set.add(index)
        current_area += block_area

    elif block_type == BLOCK_END:
        active_blocks_set.remove(index)
        current_area -= block_area

    if current_area == target_area:
        if len(active_blocks_set) < min_block_number:
            min_block_number = len(active_blocks_set)

if min_block_number == N + 1:
    print('NO')
else:
    print('YES')
    print(min_block_number)

    current_area = 0
    active_blocks_set = set()

    for ev in events:

        z_coord = ev[0]
        block_type = ev[1]
        block_area = ev[2]
        index = ev[3]

        if block_type == BLOCK_START:
            active_blocks_set.add(index)
            current_area += block_area

        elif block_type == BLOCK_END:
            active_blocks_set.remove(index)
            current_area -= block_area

        if current_area == target_area:
            if len(active_blocks_set) == min_block_number:
                min_block_number = len(active_blocks_set)
                break

    for block in sorted(list(active_blocks_set)):
        print(block + 1)








