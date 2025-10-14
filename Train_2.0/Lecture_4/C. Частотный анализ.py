from collections import defaultdict

with (open('input.txt', 'r') as f):
    my_dict = defaultdict(int)

    curr_line = f.readline().strip()
    while curr_line != '':
        words = curr_line.split()
        for word in words:
            my_dict[word] -= 1

        curr_line = f.readline().strip()

def dict_to_tuple_list(my_dict):
    tuple_list = [(count, key) for key, count in my_dict.items()]
    return tuple_list

tuple_list = dict_to_tuple_list(my_dict)
tuple_list_sorted = sorted(tuple_list)
word_list = [el[1] for el in tuple_list_sorted]

print('\n'.join(word_list))