with (open('input.txt', 'r') as f):
    ref = f.readline().strip()
    target = f.readline().strip()


def lin_search(ref, target):
    ref_index = len(ref) - 1
    index_add_after = None

    for target_index in range(len(target) - 1, -1, -1):
        if ref[ref_index] == target[target_index]:
            ref_index -= 1
            if ref_index == -1:
                ref_index = len(ref) - 1
        else:
            ref_index = len(ref) - 1
            index_add_after = target_index

    return index_add_after

index_add_after = lin_search(ref, target)
if index_add_after is not None:
    print(target[index_add_after:])
else:
    print()