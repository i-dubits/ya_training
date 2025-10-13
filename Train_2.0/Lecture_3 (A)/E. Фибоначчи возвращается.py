
import sys
sys.set_int_max_str_digits(5100)

prime_1 = 100019
prime_2 = 99989
prime_3 = 99929


def fib_brute_force(N):
    fib_set = set()
    a_n, a_n_m1 = 1, 0
    fib_set.add(a_n)
    fib_set.add(a_n_m1)

    if N == 0:
        return 0
    if N == 1:
        return 1

    for _ in range(2, N + 1):
        a_n, a_n_m1 = a_n + a_n_m1, a_n
        fib_set.add(a_n)

    return fib_set

def number_of_digits(value):
    dig_numb = 1
    while value // 10 != 0:
        value = value // 10
        dig_numb += 1

    return dig_numb

def fib_prime_number(N):
    fib_set = set()
    a_n, a_n_m1 = 1, 0

    prime_1 = 100019
    prime_2 = 99989
    prime_3 = 99929

    a_n_prime1, a_n_m1_prime1 = a_n % prime_1, a_n_m1 % prime_1
    a_n_prime2, a_n_m1_prime2 = a_n % prime_2, a_n_m1 % prime_2
    a_n_prime3, a_n_m1_prime3 = a_n % prime_3, a_n_m1 % prime_3

    fib_set.add((a_n, a_n, a_n))
    fib_set.add((a_n_m1, a_n_m1, a_n_m1))

    for _ in range(2, N + 1):
        a_n_prime1, a_n_m1_prime1 = (a_n_prime1 % prime_1 + a_n_m1_prime1 % prime_1) % prime_1, a_n_prime1
        a_n_prime2, a_n_m1_prime2 = (a_n_prime2 % prime_2 + a_n_m1_prime2 % prime_2) % prime_2, a_n_prime2
        a_n_prime3, a_n_m1_prime3 = (a_n_prime3 % prime_3 + a_n_m1_prime3 % prime_3) % prime_3, a_n_prime3

        fib_set.add( (a_n_m1_prime1, a_n_m1_prime2, a_n_m1_prime3) )

    return fib_set


# fib_set = fib_brute_force(24000)
fib_set_prime = fib_prime_number(24000)

with open('input.txt', 'r') as f:
    ans = []
    n = int(f.readline().strip())
    for _ in range(n):
        value = int(f.readline().strip())
        curr_tuple = (value % prime_1, value % prime_2, value % prime_3)
        if curr_tuple in fib_set_prime:
            ans.append('Yes')
        else:
            ans.append('No')

print('\n'.join(ans))





