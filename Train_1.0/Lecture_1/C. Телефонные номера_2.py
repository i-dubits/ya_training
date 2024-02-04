with open('input.txt', 'r') as f:
    target = f.readline().strip()
    first = f.readline().strip()
    second = f.readline().strip()
    third = f.readline().strip()

def clean_number(numb):
    new_numb = []
    for el in numb:
        if el != '(' and el != ')' and el != '-' and el != '+':
            new_numb.append(el)
    return new_numb

def compare_numbers(numb_1, numb_2):

    if len(numb_1) != 11 and len(numb_1) != 8 and len(numb_1) != 7:
        return False
    if len(numb_2) != 11 and len(numb_2) != 8 and len(numb_1) != 7:
        return False

    count_from_end = 1
    while count_from_end != 8:
        if numb_1[-count_from_end] != numb_2[-count_from_end]:
            return False
        count_from_end += 1

    if len(numb_1) == 8:
        numb_to_add = ['4', '9', '5']
        numb_1 = numb_1[:1] + numb_to_add + numb_1[1:]
    elif len(numb_1) == 7:
        numb_to_add = ['7', '4', '9', '5']
        numb_1 = numb_to_add + numb_1

    if len(numb_2) == 8:
        numb_to_add = ['4', '9', '5']
        numb_2 = numb_2[:1] + numb_to_add + numb_2[1:]
    elif len(numb_2) == 7:
        numb_to_add = ['7', '4', '9', '5']
        numb_2 = numb_to_add + numb_2

    if numb_1[0] != '7' and numb_1[0] != '8':
        if len(numb_1) != 7:
            return False
    if numb_2[0] != '7' and numb_2[0] != '8':
        if len(numb_2) != 7:
            return False

    count_from_begin = 1
    while count_from_begin != 4:
        if numb_1[count_from_begin] != numb_2[count_from_begin]:
            return False
        count_from_begin += 1

    return True



target, first, second, third = map(clean_number, [target, first, second, third])
print(f'target: {target}\n'
      f'first: {first}\n'
      f'second: {second}\n'
      f'third: {third}')

ans_1 = 'YES' if compare_numbers(target, first) else 'NO'
ans_2 = 'YES' if compare_numbers(target, second) else 'NO'
ans_3 = 'YES' if compare_numbers(target, third) else 'NO'

print(ans_1)
print(ans_2)
print(ans_3)

