
with (open('input.txt', 'r') as f):
    ref = f.readline().strip()
    target = f.readline().strip()

def prefix_function(arr):
    pref = [0] * len(arr)

    for i in range(1, len(arr)):
        j = pref[i - 1]
        while j > 0 and arr[i] != arr[j]:
            j = pref[j - 1]

        if j == 0 and arr[i] == arr[j]:
            pref[i] = 1
        elif j == 0 and arr[i] != arr[j]:
            pref[i] = 0
        elif j != 0 and arr[i] == arr[j]:
            pref[i] = j + 1

    return pref

ref_periodic = ref * ( len(target) // len(ref) + 2 )

concat_str = target + '#' + ref_periodic
pref = prefix_function(concat_str)

max_pref = pref[-1]

print(target[max_pref:])