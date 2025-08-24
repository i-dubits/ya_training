def prefix_sum_calc(arr):
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    return prefix_sum


with (open('input.txt', 'r') as f):
    arr_length, query_numb = map(int, f.readline().strip().split())
    arr = list(map(int, f.readline().strip().split()))

    prefix_sum = prefix_sum_calc(arr)
    for _ in range(query_numb):
        ind_1, ind_2 = map(int, f.readline().strip().split())
        ind_1_from_zero = ind_1 - 1
        ind_2_from_zero = ind_2 - 1

        res = prefix_sum[ind_2_from_zero + 1] - prefix_sum[ind_1_from_zero]
        print(res)
