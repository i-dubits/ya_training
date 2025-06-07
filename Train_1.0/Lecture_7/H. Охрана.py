
from collections import defaultdict

END = 1
BEGIN = 0


def process_events(events):
    events.sort()

    if events[0][0] != 0:
        print(f'Wrong Answer')
        return

    current_active_events = 0
    segm_index_to_min_count = defaultdict(int)
    active_events_set = set()

    prev_event_begin_coord = None
    events_started_now = set()

    for event in events:
        if event[1] == BEGIN:
            if prev_event_begin_coord != event[0]:
                current_active_events += 1
                active_events_set.add(event[2])

                segm_index_to_min_count[event[2]] = current_active_events

                prev_event_begin_coord = event[0]

                events_started_now = set()
                events_started_now.add(event[2])

            else:
                current_active_events += 1
                active_events_set.add(event[2])
                events_started_now.add(event[2])

                for index in events_started_now:
                    segm_index_to_min_count[index] = current_active_events

        elif event[1] == END and event[0] != 10_000:
            active_events_set.remove(event[2])
            current_active_events -= 1

            if current_active_events == 0:
                print(f'Wrong Answer')
                return
            else:
                if segm_index_to_min_count[event[2]] > 1:
                    print(f'Wrong Answer')
                    return
                else:
                    for index in active_events_set:
                        segm_index_to_min_count[index] = min(segm_index_to_min_count[index],
                                                             current_active_events)
        elif event[1] == END and event[0] == 10_000:
            active_events_set.remove(event[2])
            current_active_events -= 1

            if segm_index_to_min_count[event[2]] > 1:
                print(f'Wrong Answer')
                return

    print('Accepted')

with (open('input.txt', 'r') as f):
    segments = []

    K = int(f.readline().strip())

    for test_number in range(K):

        events = []
        inputs = list(map(int, f.readline().strip().split()))

        for i in range(2, len(inputs), 2):
            events.append( [inputs[i - 1], BEGIN, i - 1] )
            events.append( [inputs[i], END, i - 1] )

        process_events(events)





