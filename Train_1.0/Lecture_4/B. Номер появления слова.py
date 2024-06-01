

with (open('input.txt', 'r') as f):
    words = f.read().strip().split()

    word_count = {}
    res = []
    for word in words:
        if word not in word_count:
            word_count[word] = 0
            res.append(0)
        else:
            word_count[word] += 1
            res.append(word_count[word])
    print(*res)