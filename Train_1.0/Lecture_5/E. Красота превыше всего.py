
with (open('input.txt', 'r') as f):
    N, K = list(map(int, f.readline().strip().split()))
    arr = [0]
    arr.extend(list(map(int, f.readline().strip().split())))

# Dict for different for counting the trees of the specified type.
presence_dict = {k: 0 for k in range(1, K + 1)}
# If count == 0 then we have found the interval
count = K

min_length = N
min_left_index = 1
min_right_index = N

left = 1
right = 1

last_right_processed = -1
last_left_processed = -1

while left < N + 1:
    while right < N + 1:
        if last_right_processed != right:
            if presence_dict[arr[right]] == 0:
                count -= 1
            presence_dict[arr[right]] += 1
            last_right_processed = right

        if count == 0:
            curr_length = right - left + 1
            if min_length > curr_length:
                min_length = curr_length
                min_left_index = left
                min_right_index = right

            break

        right += 1

    if min_length == K:  # minimal possible length
        break

    if last_left_processed != left and presence_dict[arr[left]] == 1:
        count += 1
    presence_dict[arr[left]] -= 1
    last_left_processed = left
    left += 1

print(min_left_index, min_right_index)



