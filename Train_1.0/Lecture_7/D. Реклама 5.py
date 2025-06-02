import copy
from collections import defaultdict
from collections import Counter
import copy

EVENT_BEGIN = -1
EVENT_END = 1
EVENT_REMOVE = 2

distance = 5
with (open('input.txt', 'r') as f):
    events = []

    N = int(f.readline().strip())
    for index in range(N):
        begin, end = list(map(int, f.readline().strip().split()))
        end -= distance
        if end >= 0 and begin <= end:
            events.append( (begin, EVENT_BEGIN, index) )
            events.append( (end, EVENT_END, index) )
            events.append( (end, EVENT_REMOVE, index) )


events.sort()

global_count = 0
event_1_top_count = 0
event_2_top_count = 0
event_1_start = None
event_2_start = None


active_segments_event_1 = set()
for i in range(len(events)):
    if events[i][1] == EVENT_BEGIN:
        active_segments_event_1.add(events[i][2])
        event_1_top_count = len(active_segments_event_1)

        if event_1_top_count > global_count:
            event_1_start = events[i][0]
            global_count = event_1_top_count

    if events[i][1] == EVENT_END:
        if events[i][2] not in active_segments_event_1:
            active_segments_event_1.add(events[i][2])

        event_1_top_count = len(active_segments_event_1)
        if event_1_top_count > global_count:
            event_1_start = events[i][0]
            global_count = event_1_top_count

    if events[i][1] == EVENT_REMOVE:
        if events[i][2] in active_segments_event_1:
            active_segments_event_1.remove(events[i][2])

    if events[i][1] != EVENT_REMOVE:
        active_segments_event_2 = set()
        event_2_top_count = 0
        for j in range(i + 1, len(events)):

            if events[j][2] not in active_segments_event_1:
                if events[j][1] == EVENT_BEGIN:
                    active_segments_event_2.add(events[j][2])
                    if events[i][0] + distance <= events[j][0]:
                        event_2_top_count = len(active_segments_event_2)

                        if event_1_top_count + event_2_top_count > global_count:
                            global_count = event_1_top_count + event_2_top_count
                            event_1_start = events[i][0]
                            event_2_start = events[j][0]


                if events[j][1] == EVENT_END:
                    if events[i][0] + distance <= events[j][0]:
                        if events[j][2] not in active_segments_event_2:
                            active_segments_event_2.add(events[j][2])

                        event_2_top_count = len(active_segments_event_2)

                        if event_1_top_count + event_2_top_count > global_count:
                            global_count = event_1_top_count + event_2_top_count
                            event_1_start = events[i][0]
                            event_2_start = events[j][0]

                if events[j][1] == EVENT_REMOVE:
                    if events[j][2] in active_segments_event_2:
                            active_segments_event_2.remove(events[j][2])



if event_1_start is None and event_2_start is None:
    print(f'{global_count} {10} {100}')
elif event_2_start is None:
    print(f'{global_count} {event_1_start} {event_1_start + 100}')
else:
    print(f'{global_count} {event_1_start} {event_2_start}')





n = int(input())
events = []

for i in range(n):
    nowin, nowout = map(int, input().split())
    if nowout - nowin >= 5:
        events.append((nowin, -1, i))
        events.append((nowout - 5, 1, i))

events.sort()

if len(events) == 0:
    print(0, 10, 20)
elif len(events) == 2:
    print(1, events[0][0], events[0][0] + 10)
else:
    bestans = 0
    firstbest, secondbest = 0, 0
    firstad = set()

    for i in range(len(events)):
        event1 = events[i]
        if event1[1] == -1:
            firstad.add(event1[2])

            if len(firstad) > bestans:
                bestans = len(firstad)
                firstbest = event1[0]
                secondbest = event1[0] + 5

            secondadcnt = 0

            for j in range(i + 1, len(events)):
                event2 = events[j]

                if event2[1] == -1 and event2[2] not in firstad:
                    secondadcnt += 1

                if event2[0] - 5 >= event1[0] and len(firstad) + secondadcnt > bestans:
                    bestans = len(firstad) + secondadcnt
                    firstbest = event1[0]
                    secondbest = event2[0]

                if event2[1] == 1 and event2[2] not in firstad:
                    secondadcnt -= 1

        if event1[1] == 1:
            firstad.remove(event1[2])

    print(bestans, firstbest, secondbest)
