
with (open('input.txt', 'r') as f):
    arr = list(map(int, f.readline().strip().split()))

house_dist = {i: 0 for i in range(len(arr))}


# Left to right pass
curr_dist_left = len(arr) + 1
for i in range(len(arr)):
    if arr[i] == 2:
        curr_dist_left = 0
    elif arr[i] == 0:
        curr_dist_left += 1
    elif arr[i] == 1:
        curr_dist_left += 1
        house_dist[i] = curr_dist_left

# Right to left pass
curr_dist_right = len(arr) + 1
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 2:
        curr_dist_right = 0
    elif arr[i] == 0:
        curr_dist_right += 1
    elif arr[i] == 1:
        curr_dist_right += 1
        house_dist[i] = min(house_dist[i], curr_dist_right)

# max dist
res_index = max(house_dist, key = house_dist.get)
print(house_dist[res_index])


