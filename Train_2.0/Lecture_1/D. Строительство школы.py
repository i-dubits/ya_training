

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

def calc_dist(arr, index):

    dist = 0
    target_value = arr[index]

    for i in range(len(arr)):
        if i < index:
            dist += target_value - arr[index]
        elif i > index:
            dist += arr[index] - target_value
        elif i == index:
            pass

    return dist


def median(arr):

    if len(arr) % 2 != 0:
        med_ind_start_index_1 = (len(arr) // 2) + 1
        med_ind_start_index_0 = med_ind_start_index_1 - 1

        return med_ind_start_index_0
    else:
        med_ind_cand_1_start_index_0 = (len(arr) // 2) - 1
        med_ind_cand_2_start_index_0 = (len(arr) // 2 + 1) - 1

        dist_1 = calc_dist(arr, med_ind_cand_1_start_index_0)
        dist_2 = calc_dist(arr, med_ind_cand_2_start_index_0)

        if dist_1 < dist_2:
            return med_ind_cand_1_start_index_0
        else:
            return med_ind_cand_2_start_index_0

index = median(arr)
print(arr[index])