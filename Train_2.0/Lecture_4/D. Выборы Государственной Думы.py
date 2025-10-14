
from collections import defaultdict

with (open('input.txt', 'r') as f):
    party_votes = defaultdict(int)

    curr_line = f.readline().strip()
    while curr_line != '':
        name_votes = curr_line.split()
        name = ' '.join(name_votes[:-1])
        votes = int(name_votes[-1])
        party_votes[name] += votes
        curr_line = f.readline().strip()

total_votes = sum(party_votes.values())

party_places = {}
remaining_seats = 450
for party_name, votes in party_votes.items():
    nominator = 450 * party_votes[party_name]
    final = nominator // total_votes
    party_places[party_name] = [final, nominator // total_votes, nominator % total_votes]

    remaining_seats -= party_places[party_name][0]

if remaining_seats != 0:
    priority_to_party = []
    for party_name, party_list in party_places.items():
        curr_tuple = (party_list[2], party_votes[party_name], party_name)
        priority_to_party.append(curr_tuple)

    priority_to_party = sorted(priority_to_party)

    while remaining_seats != 0:
        for curr_tuple in priority_to_party[::-1]:
            if remaining_seats == 0:
                break
            party_name = curr_tuple[2]
            party_places[party_name][0] += 1
            remaining_seats -= 1

ans = []
for party_name, seats in party_places.items():
    res = party_name + ' ' +  str(seats[0])
    ans.append(res)

print('\n'.join(ans))

