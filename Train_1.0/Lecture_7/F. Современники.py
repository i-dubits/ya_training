
START = 1
END = 0

DEBUG = False
# DEBUG = True

def calc_age(d_1, m_1, y_1, d_2, m_2, y_2):
    age = y_2 - y_1
    if (m_2, d_2) < (m_1, d_1):
        age -= 1

    return age

def def_to_number(d, m, y):
    return y * 10000 + m * 100 + d

def preproc_test_events(test_events):
    N = len(test_events)
    test_events_new = []
    for index in range(N):
        test_events_new.append( (test_events[index][0], START, index) )
        test_events_new.append( (test_events[index][1], END, index) )

    test_events_new.sort()
    return test_events_new

with (open('input.txt', 'r') as f):

    N = int(f.readline().strip())
    events = []
    for index in range(1, N + 1):
        d_1, m_1, y_1, d_2, m_2, y_2  = list(map(int, f.readline().strip().split()))
        age = calc_age(d_1, m_1, y_1, d_2, m_2, y_2)
        if age < 18:
            continue

        y_1 = y_1 + 18

        if age < 80:
            pass
        else:
            d_2, m_2, y_2 = d_1, m_1, (y_1 - 18) + 80

        date_start = def_to_number(d_1, m_1, y_1)
        date_end = def_to_number(d_2, m_2, y_2)
        events.append( (date_start, START, index) )
        events.append((date_end, END, index))


events.sort()
#print(events)

list_of_sets = []
current_set = set()
used_segments = set()
prev_ev_type = None

if DEBUG:
    # TEST EVENTS
    events = [(1, 5), (2, 6), (3, 9), (7, 10)]
    events = preproc_test_events(events)

for ev in events:
    if ev[1] == START:
        current_set.add(ev[2])
        prev_ev_type = START

    if ev[1] == END:
        if prev_ev_type == START:
            list_of_sets.append(current_set.copy())

        prev_ev_type = END
        current_set.remove(ev[2])

if all([s is None for s in list_of_sets]):
    print(0)
else:
    for sets in list_of_sets:
        if sets is not None:
            print(' '.join( [str(s) for s in sets]))

