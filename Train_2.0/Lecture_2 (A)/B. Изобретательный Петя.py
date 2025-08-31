

with (open('input.txt', 'r') as f):
    ref = f.readline().strip()
    target = f.readline().strip()


def find_coinc(ref, target, ref_char_index):
    index_last_coinc = 0

    ref_index = ref_char_index + 1
    if ref_index == len(ref):
        ref_index = 0

    while index_last_coinc + 1 < len(target) and ref[ref_index] == target[index_last_coinc + 1]:
        index_last_coinc += 1
        ref_index += 1
        if ref_index == len(ref):
            ref_index = 0

    if ref_index == 0:
        return index_last_coinc
    else:
        return index_last_coinc - ref_index

max_index_last_coinc = -1
for ref_char_index, ref_char in enumerate(ref):
    if ref_char == target[0]:
        index_last_coinc = find_coinc(ref, target, ref_char_index)
        max_index_last_coinc = max(index_last_coinc, max_index_last_coinc)

if max_index_last_coinc == -1:
    print(target)
else:
    print(target[max_index_last_coinc + 1:])