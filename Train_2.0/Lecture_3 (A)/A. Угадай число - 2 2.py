from time import perf_counter



with (open('input.txt', 'r') as f):

    N = int(f.readline().strip())

    answer = set(i for i in range(1, N + 1))
    answer_length = len(answer)

    while True:
        curr_line = f.readline().strip()
        if curr_line[0] == 'H':
            break

        curr_set = set(map( int, curr_line.split()))
        yes_count = 0
        for el in curr_set:
            if el in answer:
                yes_count += 1

        if 2 * yes_count > answer_length:
            answer.intersection_update(curr_set)
            answer_length = yes_count
            print('YES')
        else:
            answer.difference_update(curr_set)
            answer_length = answer_length - yes_count
            print('NO')


answer_list = list(answer)
print(*sorted(answer_list))
