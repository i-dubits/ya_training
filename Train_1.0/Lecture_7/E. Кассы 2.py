COUNTER_CLOSE = 0
COUNTER_OPEN = 3

COUNTER_PSEUDOCLOSE_MIDNIGHT = 4
COUNTER_PSEUDOPEN_MIDNIGHT = 1

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
        elif begin_min > end_min:
            if end_min != 0:
                events.append((begin_min, COUNTER_OPEN, index))
                events.append((end_min, COUNTER_CLOSE, index))

                events.append((0, COUNTER_PSEUDOPEN_MIDNIGHT, index))
                events.append((23*60 + 59, COUNTER_PSEUDOCLOSE_MIDNIGHT, index))
            else:
                events.append((begin_min, COUNTER_OPEN, index))
                events.append((end_min, COUNTER_CLOSE, index))

        elif begin_min < end_min:
            events.append((begin_min, COUNTER_OPEN, index))
            events.append((end_min, COUNTER_CLOSE, index))


events.sort()

target_counters_number = N - full_day_count
start_time_all_counters_open = None
total_time = 0
open_counters = set()

for ev in events:
    if ev[1] == COUNTER_CLOSE:
        index = ev[2]
        if index in open_counters:
            if target_counters_number == len(open_counters):
                total_time += ev[0] - start_time_all_counters_open

            if index in open_counters:
                open_counters.remove(index)
            start_time_all_counters_open = None

    elif ev[1] == COUNTER_OPEN or ev[1] == COUNTER_PSEUDOPEN_MIDNIGHT:
        index = ev[2]
        open_counters.add(index)
        if len(open_counters) == target_counters_number:
            start_time_all_counters_open = ev[0]

    elif ev[1] == COUNTER_PSEUDOCLOSE_MIDNIGHT:
        index = ev[2]
        if index in open_counters:
            if target_counters_number == len(open_counters):
                total_time += ev[0] - start_time_all_counters_open + 1

            if index in open_counters:
                open_counters.remove(index)
            start_time_all_counters_open = None


if len(open_counters) == target_counters_number and start_time_all_counters_open is not None:
    total_time += 24*60 - start_time_all_counters_open

if total_time == 0 and full_day_count != 0:
    print(24*60)
else:
    print(total_time)