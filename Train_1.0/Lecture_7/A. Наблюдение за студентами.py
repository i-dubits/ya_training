
EVENT_BEGIN = -1
EVENT_END = 1

with (open('input.txt', 'r') as f):
    N, M = map(int, f.readline().strip().split())

    events = []

    for _ in range(M):
        beg, end = map(int, f.readline().strip().split())
        events.append((beg, EVENT_BEGIN))
        events.append((end, EVENT_END))

events_sorted = sorted(events)

total_length = 0
begin_current = None
total_count = 0

for ev in events_sorted:
    if ev[1] == EVENT_BEGIN:
        if total_count == 0:
            begin_current = ev[0]

        total_count += 1

    elif ev[1] == EVENT_END:
        total_count -= 1

        if total_count == 0:
            total_length += ev[0] - begin_current + 1
            begin_current = None

print(N - total_length)


