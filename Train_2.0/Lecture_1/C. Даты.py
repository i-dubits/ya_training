


with (open('input.txt', 'r') as f):
    first, second, year = map(int, f.readline().strip().split())

leap_years = {i for i in range(1972, 2070, 4)}
month_length = {1:31, 2:None, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}



def correct_Eur(day, month, year):
    if month > 12:
        return False
    else:
        if month != 2:
            if day <= month_length[month]:
                return True
            else:
                return False
        else:
            if year in leap_years:
                if day <= 29:
                    return True
                else:
                    return False
            else:
                if day <= 28:
                    return True
                else:
                    return False


def correct_US(day, month, year):
    ans = correct_Eur(month, day, year)

    return ans

if first == second:
    print(f'1')
elif correct_Eur(first, second, year) and correct_US(first, second, year):
    print(f'0')
else:
    print(f'1')
