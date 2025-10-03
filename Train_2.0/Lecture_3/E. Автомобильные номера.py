

def plate_witn_numb(plate_set: set, witness_sets: list[set]):
    number_of_witn = 0
    for w_set in witness_sets:
        if w_set.intersection(plate_set) == w_set:
            number_of_witn += 1

    return number_of_witn


plate_strings = []
with open('input.txt', 'r') as f:
    witness_number = int(f.readline().strip())

    witness_sets = []
    for i in range(witness_number):
        witness_sets.append(set(f.readline().strip()))

    plate_number = int(f.readline().strip())

    plate_sets = []
    for i in range(plate_number):
        curr_string = f.readline().strip()
        plate_strings.append(curr_string)
        plate_sets.append(set(curr_string))

def find_plates(plate_sets, witness_sets, plate_strings):
    max_count = 0
    plate_ind_count = [0] * len(plate_sets)
    for plate_ind, plate in enumerate(plate_sets):
        curr_numb = plate_witn_numb(plate, witness_sets)
        plate_ind_count[plate_ind] = curr_numb
        max_count = max(max_count, curr_numb)

    for plate_ind, plate in enumerate(plate_sets):
        if plate_ind_count[plate_ind] == max_count:
            print(plate_strings[plate_ind])

find_plates(plate_sets, witness_sets, plate_strings)



