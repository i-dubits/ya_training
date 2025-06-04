with (open('input.txt', 'r') as f):

    target_balloon_count, person_count = map(int, f.readline().strip().split())
    events = []
    person_dict = {}
    full_day_count = 0
    for index in range(person_count):
        t_per_one, max_balloons_in_a_row, t_cooldown = list(map(int, f.readline().strip().split()))
        person_dict[index] = {'Z': max_balloons_in_a_row, 'T': t_per_one, 'Y': t_cooldown,
                              'full_cycle_time': max_balloons_in_a_row * t_per_one + t_cooldown,
                              'produced': 0}


def check(given_time):
    total_produced = 0
    for index, pers_data in person_dict.items():
        full_cycle_count = given_time // pers_data['full_cycle_time']
        total_produced += pers_data['Z'] * full_cycle_count

        last_cycle_time = given_time % pers_data['full_cycle_time']
        if last_cycle_time >= pers_data['Z'] * pers_data['T']:
            total_produced += pers_data['Z']
        else:
            total_produced += last_cycle_time // pers_data['T']

        if total_produced >= target_balloon_count:
            return True, total_produced

    return False, total_produced

def production_at_time(given_time):
    total_count = 0
    for index, pers_data in person_dict.items():
        full_cycle_count = given_time // pers_data['full_cycle_time']
        pers_data['produced'] += pers_data['Z'] * full_cycle_count
        total_count += pers_data['Z'] * full_cycle_count
        if total_count >= target_balloon_count:
            pers_data['produced'] -= total_count - target_balloon_count
            break

        last_cycle_time = given_time % pers_data['full_cycle_time']
        if last_cycle_time >= pers_data['Z'] * pers_data['T']:
            pers_data['produced'] += pers_data['Z']
            total_count += pers_data['Z']
            if total_count >= target_balloon_count:
                pers_data['produced'] -= total_count - target_balloon_count
                break
        else:
            pers_data['produced'] += last_cycle_time // pers_data['T']
            total_count += last_cycle_time // pers_data['T']
            if total_count >= target_balloon_count:
                pers_data['produced'] -= total_count - target_balloon_count
                break

    return person_dict

l = -1
r = 250 * 15_0000

while l < r - 1:
    m = l + (r - l) // 2

    if check(m)[0]:
        r = m
    else:
        l = m


print(r)
person_dict = production_at_time(r)
print(' '.join([str(pers_info['produced']) for pers, pers_info in person_dict.items()]))



