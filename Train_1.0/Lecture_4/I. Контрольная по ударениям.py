import re


with open('input.txt', 'r') as f:
    cap_letter_dict = {}
    N = int(f.readline().strip())
    for i in range(N):
        curr_word = f.readline().strip()
        cap_letters = re.finditer('([A-Z])', curr_word)
        curr_word_positions_list = [cap_letter.span()[0] for cap_letter in cap_letters]
        if curr_word.lower() not in cap_letter_dict:
            cap_letter_dict[curr_word.lower()] = curr_word_positions_list
        else:
            cap_letter_dict[curr_word.lower()].extend(curr_word_positions_list)

    phrase = f.readline().strip().split(' ')

err_counter = 0
for curr_word in phrase:
    if curr_word != '':
        if curr_word.lower() in cap_letter_dict:
            cap_letters = re.finditer('([A-Z])', curr_word)
            curr_word_positions_list = [cap_letter.span()[0] for cap_letter in cap_letters]
            if len(curr_word_positions_list) != 1:
                err_counter += 1
            else:
                if curr_word_positions_list[0] in cap_letter_dict[curr_word.lower()]:
                    pass
                else:
                    err_counter += 1

        else:
            cap_letters = re.finditer('([A-Z])', curr_word)
            curr_word_positions_list = [cap_letter.span()[0] for cap_letter in cap_letters]
            if len(curr_word_positions_list) != 1:
                err_counter += 1

print(err_counter)
