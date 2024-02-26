

with open('input.txt', 'r') as f:
    n, k, m = map(int, f.readline().strip().split())

def get_det_steel(number_of_prep):
    number_det = (k // m) * number_of_prep
    remain_steel_det = (k % m) * number_of_prep

    return number_det, remain_steel_det

def get_prep_steel(number_of_coal):
    number_prep = number_of_coal // k
    remain_steel_prep = number_of_coal % k

    return number_prep, remain_steel_prep

number_det_total = 0
number_of_coal = n

if k < m or n < k:
    print(0)
else:
    while number_of_coal // k != 0:
        number_prep, remain_steel_prep = get_prep_steel(number_of_coal)
        number_det, remain_steel_det = get_det_steel(number_prep)

        number_det_total += number_det

        number_of_coal = remain_steel_prep + remain_steel_det

    print(number_det_total)


