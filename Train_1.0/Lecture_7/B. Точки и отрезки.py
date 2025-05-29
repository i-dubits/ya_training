from collections import defaultdict

EVENT_BEGIN = -1
EVENT_END = 1
EVENT_POINT = 0

with (open('input.txt', 'r') as f):
    N, M = map(int, f.readline().strip().split())

    events = []

    for _ in range(N):
        beg, end = map(int, f.readline().strip().split())
        if beg > end:
            beg, end = end, beg
        events.append((beg, EVENT_BEGIN))
        events.append((end, EVENT_END))

    points = list(map(int, f.readline().strip().split()))
    for p in points:
        events.append((p, EVENT_POINT))


events_sorted = sorted(events)

ans = defaultdict(int)
total_count = 0

for ev in events_sorted:

    if ev[1] == EVENT_BEGIN:
        total_count += 1

    elif ev[1] == EVENT_POINT:
        ans[ev[0]] = total_count

    elif ev[1] == EVENT_END:
        total_count -= 1

print(' '.join([str(ans[p]) for p in points]))
