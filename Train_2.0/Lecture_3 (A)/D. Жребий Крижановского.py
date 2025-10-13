from collections import Counter
from collections import defaultdict

def count_less_than_given(target_score, scores):
    count = 0
    for score in scores:
        if score < target_score:
            count += 1

    return count


def find_winner(player_to_guess):
    guess_to_count = defaultdict(int)
    winner_cand = (None, None)  # player ind, value

    for player_id, guess in player_to_guess.items():
        guess_to_count[guess] += 1

    for player_id, guess in player_to_guess.items():
        if guess_to_count[guess] == 1:
            if winner_cand[0] is None or winner_cand[1] > guess:
                winner_cand = (player_id, guess)

    return winner_cand


def update_scores(player_to_score, player_to_guess):

    new_player_to_score = player_to_score.copy()

    winner = find_winner(player_to_guess)
    if winner[0] is not None:
        new_player_to_score[winner[0]] += winner[1]

    return new_player_to_score


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())

    player_to_score = {}
    for indx, el in enumerate(f.readline().strip().split()):
        player_to_score[indx + 1] = int(el)

    player_to_guess = {}
    for indx, el in enumerate(f.readline().strip().split()):
        player_to_guess[indx + 1] = int(el)

count_max = None
ans = 1

for possible_score in range(1, 202):
    player_to_guess[n] = possible_score

    winner_cand = find_winner(player_to_guess)
    new_player_to_score = update_scores(player_to_score, player_to_guess)

    count_current = count_less_than_given(new_player_to_score[len(new_player_to_score)],
                                          new_player_to_score.values())
    if count_max is None or count_current > count_max:
        count_max = count_current
        ans = possible_score

print(ans)