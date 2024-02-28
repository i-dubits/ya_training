curr = 0
answ_dict = {'const': True, 'asc': True, 'dsc': True, 'wasc': True, 'wdsc': True}

with open('input.txt', 'r') as f:
    prev = int(f.readline().strip())
    while True:
        curr = int(f.readline().strip())
        if curr == -2000000000:
            break
        else:
            if curr > prev:
                answ_dict['const'] = False
                answ_dict['dsc'] = False
                answ_dict['wdsc'] = False
            elif curr < prev:
                answ_dict['const'] = False
                answ_dict['asc'] = False
                answ_dict['wasc'] = False
            elif curr == prev:
                answ_dict['asc'] = False
                answ_dict['dsc'] = False
            prev = curr


def check_dict(answ_dict):
    if all(value == False for value in answ_dict.values()):
        print('RANDOM')
        return

    if answ_dict['const'] == True:
        print('CONSTANT')
        return

    if answ_dict['asc'] == True and answ_dict['wasc'] == True:
        print('ASCENDING')
        return
    if answ_dict['asc'] == False and answ_dict['wasc'] == True:
        print('WEAKLY ASCENDING')
        return
    if answ_dict['dsc'] == True and answ_dict['wdsc'] == True:
        print('DESCENDING')
        return
    if answ_dict['dsc'] == False and answ_dict['wdsc'] == True:
        print('WEAKLY DESCENDING')
        return

check_dict(answ_dict)
