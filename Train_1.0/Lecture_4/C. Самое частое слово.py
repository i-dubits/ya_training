from collections import Counter

with (open('input.txt', 'r') as f):
    words = f.read().strip().split()

cnt = Counter(words)
max_val = cnt.most_common(1)[0][1]

best_el = []
for word, value in cnt.items():
    if value < max_val:
        pass
    elif value == max_val:
        if best_el:
            best_el = best_el if best_el < word else word
        else:
            best_el = word
print(best_el)
