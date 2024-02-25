import math
from icecream import ic

with open('input.txt', 'r') as f:
    k_1, m, k_2, p_2, n_2 = map(int, f.readline().strip().split())

def get_p_n(k, m, T):
    floor = (k - 1) // T + 1
    p = (floor - 1) // m + 1
    n = (floor - 1) % m + 1

    return p, n


def calc_all():
    c_2 = (p_2 - 1) * m + (n_2 - 1)
    ic(c_2)

    if c_2 == 0:
        if m == 1:
            if k_1 <= k_2:
                print(*[1, 1])
                return
            else:
                print(*[0, 1])
                return
        else:
            if k_1 <= k_2:
                print(*[1, 1])
                return
            elif k_1 <= m:
                print(*[1, 0])
                return
            else:
                print(*[0, 0])
                return
    else:
        max_T = k_2//c_2 if k_2 % c_2 != 0 else k_2//c_2 - 1
        min_T = math.ceil(k_2/(c_2 + 1))

        min_x2 = k_2 - c_2 * max_T
        max_x2 = k_2 - c_2 * min_T

        ic(min_T)
        ic(max_T)
        ic(min_x2)
        ic(max_x2)

        if max_x2 == 0 or min_T > max_T:
            print(*[-1, -1])
            return
        else:
            p_set = set()
            n_set = set()
            for T_curr in range(min_T, max_T + 1):
                p_2_pred, n_2_pred = get_p_n(k_2, m, T_curr)
                if p_2_pred != p_2 or n_2_pred != n_2:
                    print(*[-1, -1])
                    return
                else:
                    p_1_pred, n_1_pred = get_p_n(k_1, m, T_curr)
                    p_set.add(p_1_pred)
                    n_set.add(n_1_pred)

            if len(p_set) == 1:
                p_1 = p_set.pop()
            else:
                p_1 = 0

            if len(n_set) == 1:
                n_1 = n_set.pop()
            else:
                n_1 = 0

            print(*[p_1, n_1])
            return

calc_all()