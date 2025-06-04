

COUNTER_CLOSE = -1
COUNTER_OPEN = 1

with (open('input.txt', 'r') as f):
    segments = []

    N = int(f.readline().strip())
    events = []
    full_day_count = 0
    for index in range(N):
        hour_1, min_1, hour_2, min_2 = list(map(int, f.readline().strip().split()))
        begin_min = hour_1 * 60 + min_1
        end_min = hour_2 * 60 + min_2

        if begin_min == end_min:
            full_day_count +=  1
        else:
            events.append((begin_min, COUNTER_OPEN, index))
            events.append((end_min, COUNTER_CLOSE, index))


events = sorted(events)

target_counters_number = N - full_day_count
start_time_all_counters_open = None
total_time = 0
open_counters = set()
all_time_intervals = set()

for ev in events:
    if ev[1] == COUNTER_CLOSE:
        index = ev[2]
        if index in open_counters:
            if (target_counters_number == len(open_counters)
                    and (start_time_all_counters_open, ev[0]) not in all_time_intervals):
                all_time_intervals.add((start_time_all_counters_open, ev[0]))
                total_time += ev[0] - start_time_all_counters_open

            open_counters.remove(index)
            start_time_all_counters_open = None

    elif ev[1] == COUNTER_OPEN:
        index = ev[2]
        open_counters.add(index)
        if len(open_counters) == target_counters_number:
            start_time_all_counters_open = ev[0]

for ev in events:
    if ev[1] == COUNTER_CLOSE:
        index = ev[2]
        if index in open_counters:
            if (target_counters_number == len(open_counters)
                    and (start_time_all_counters_open, ev[0]) not in all_time_intervals):
                all_time_intervals.add((start_time_all_counters_open, 0))
                all_time_intervals.add((ev[0], 0))


                if ev[0] < start_time_all_counters_open:
                    total_time += 24*60 - start_time_all_counters_open + (ev[0] - 0)
                else:
                    total_time += ev[0] - start_time_all_counters_open

            open_counters.remove(index)
            start_time_all_counters_open = None

    elif ev[1] == COUNTER_OPEN:
        index = ev[2]
        open_counters.add(index)
        if len(open_counters) == target_counters_number:
            start_time_all_counters_open = ev[0]


if total_time == 0 and full_day_count != 0:
    print(24*60)
else:
    print(total_time)