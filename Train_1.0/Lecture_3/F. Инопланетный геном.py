with open('input.txt', 'r') as f:
    source = f.readline().strip()
    target = f.readline().strip()

src_dict = {}
for i in range(0, len(source) - 1):
    if source[i:i+2] in src_dict:
        src_dict[source[i:i+2]] += 1
    else:
        src_dict[source[i:i + 2]] = 1

res = 0
for i in range(0, len(target) - 1):
    if target[i:i+2] in src_dict:
        res += src_dict[target[i:i+2]]
        del src_dict[target[i:i+2]]

print(res)
