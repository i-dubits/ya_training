#
#
#
# from collections import defaultdict
#
# END = 1
# BEGIN = 0
#
#
# def process_events(events, total_number_of_segments):
#     events.sort()
#
#     if events[0][0] != 0:
#         print(f'Wrong Answer')
#         return
#
#     current_active_events = 0
#     active_events_set = set()
#     single_segments = set()
#     end_at_given_point = set()
#     prev_coord = -1
#
#     for ev in events:
#         coord = ev[0]
#         event_type = ev[1]
#         index = ev[2]
#
#         if event_type == BEGIN:
#             if coord == 0:
#                 active_events_set.add(index)
#                 continue
#
#             if len(active_events_set) == 0:
#                 print(f'Wrong Answer')
#                 return
#             elif len(active_events_set) == 1:
#                 single_segments.update(active_events_set)
#                 active_events_set.add(index)
#             elif len(active_events_set) > 1:
#                 active_events_set.add(index)
#
#         elif event_type == END:
#             if len(active_events_set) == 1 and prev_coord != coord:
#                 single_segments.update(active_events_set)
#                 active_events_set.remove(index)
#             elif len(active_events_set) > 1:
#                 prev_coord = coord
#                 active_events_set.remove(index)
#
#     if events[-1][0] != 10_000:
#         print(f'Wrong Answer')
#         return
#     if len(single_segments) != total_number_of_segments:
#         print(f'Wrong Answer')
#         return
#     else:
#         print(f'Accepted')
#         return
#
#
#
# with (open('input.txt', 'r') as f):
#     segments = []
#
#     K = int(f.readline().strip())
#
#     for test_number in range(K):
#
#         events = []
#         inputs = list(map(int, f.readline().strip().split()))
#         total_number_of_segments = inputs[0]
#
#         for i in range(2, len(inputs), 2):
#             events.append( [inputs[i - 1], BEGIN, i - 1] )
#             events.append( [inputs[i], END, i - 1] )
#
#         process_events(events, total_number_of_segments)

k = int(input())
ans = [''] * k
for test in range(k):
    nums = list(map(int, input().split()))
    n = nums[0]
    events = [0] * (2 * n)
    for i in range(1, len(nums), 2):
        events[i - 1] = (nums[i], -1, i)
        events[i] = (nums[i + 1], 1, i)
    events.sort()
    goodseq = set()
    nowseq = set()
    goodflag = True
    prevtime = -1
    for event in events:
        if event[0] != 0 and len(nowseq) == 0:
            goodflag = False
            break
        if len(nowseq) == 1 and event[0] != prevtime:
            goodseq.update(nowseq)
        if event[1] == -1:
            nowseq.add(event[2])
        else:
            nowseq.remove(event[2])
        prevtime = event[0]
    if events[-1][0] != 10_000:
        goodflag = False
    if goodflag and len(goodseq) == n:
        ans[test] = 'Accepted'
    else:
        ans[test] = 'Wrong Answer'
print('\n'.join(ans))

