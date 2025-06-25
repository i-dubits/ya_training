from collections import defaultdict

DEPART = 1
ARRIVED = 0

with (open('input.txt', 'r') as f):

    city_count, route_count = map(int, f.readline().strip().split())

    events = []
    for i in range(route_count):
        inputs = list(f.readline().strip().split())
        from_city = int(inputs[0])
        to_city = int(inputs[2])
        from_time = inputs[1].split(':')
        from_time = int(from_time[0]) * 60 + int(from_time[1])
        to_time = inputs[3].split(':')
        to_time = int(to_time[0]) * 60 + int(to_time[1])

        events.append( (from_time, DEPART, from_city, i) ) # city, time, type, index of route
        events.append( (to_time, ARRIVED, to_city, i) ) # city, time, type, index of route

events.sort()

active_routes = set()
bus_count = 0

city_to_number_of_free_busses = defaultdict(int)

for i in range(2):
    for ev in events:

        if ev[1] == DEPART:
            active_routes.add(ev[3])
            if city_to_number_of_free_busses[ev[2]] >= 1:
                city_to_number_of_free_busses[ev[2]] -= 1
            else:
                bus_count += 1

        if ev[1] == ARRIVED:
            if ev[3] in active_routes:
                active_routes.remove(ev[3])
                city_to_number_of_free_busses[ev[2]] += 1

bus_count_after_two_runs = bus_count

for i in range(2):
    for ev in events:

        if ev[1] == DEPART:
            active_routes.add(ev[3])
            if city_to_number_of_free_busses[ev[2]] >= 1:
                city_to_number_of_free_busses[ev[2]] -= 1
            else:
                bus_count += 1

        if ev[1] == ARRIVED:
            if ev[3] in active_routes:
                active_routes.remove(ev[3])
                city_to_number_of_free_busses[ev[2]] += 1

if bus_count_after_two_runs != bus_count:
    print(-1)
else:
    print(bus_count)





