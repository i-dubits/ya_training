import heapq


with (open('input.txt', 'r') as f):

    target_balloon_count, person_count = map(int, f.readline().strip().split())
    events = []
    person_dict = {}
    full_day_count = 0
    for index in range(person_count):
        t_per_one, max_balloons_in_a_row, t_cooldown = list(map(int, f.readline().strip().split()))
        person_dict[index] = {'t_per_one': t_per_one, 'max_balloons_in_a_row': max_balloons_in_a_row,
                              't_cooldown': t_cooldown, 'produced_total': 0,
                              'produced_in_a_row': 0}

        end_time_one_balloon = t_per_one
        events.append( (end_time_one_balloon, index) )

heapq.heapify(events)

current_balloon_count = 0
current_time = 0

while current_balloon_count < target_balloon_count:
    curr_event = heapq.heappop(events)
    index = curr_event[1]

    if current_time != curr_event[0]:
        current_time = curr_event[0]

    person_dict[index]['produced_total'] += 1
    person_dict[index]['produced_in_a_row'] += 1

    if person_dict[index]['max_balloons_in_a_row'] == person_dict[index]['produced_in_a_row']:
        end_time = current_time + person_dict[index]['t_cooldown'] + person_dict[index]['t_per_one']
        new_event = (end_time, index)
        heapq.heappush(events, new_event)
        person_dict[index]['produced_in_a_row'] = 0

    else:
        end_time = current_time + person_dict[index]['t_per_one']
        new_event = (end_time, index)
        heapq.heappush(events, new_event)


    current_balloon_count += 1

print(current_time)

print(' '.join([str(pers_info['produced_total']) for pers, pers_info in person_dict.items()]) )







