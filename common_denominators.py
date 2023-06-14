import numpy as np
from math import prod

def convert_fracts(lst):
    # first round of simplification
    new_lst = []
    for i in lst:
        if np.gcd(i[0], i[1]) != 1:
            first = i[0]/np.gcd(i[0], i[1])
            second = i[1]/np.gcd(i[0], i[1])
            i[0] = int(first)
            i[1] = int(second)
        new_lst.append(i)

    # finding the gcp of the total
    denominator = int(prod([i[1] for i in new_lst]))
    numerator = int(sum([i[0]*denominator/i[1] for i in new_lst]))
    gcd = np.gcd(numerator, denominator)
    den_final = int(denominator/gcd)
    return [[int(i[0]*den_final/i[1]), den_final] for i in new_lst]


if __name__ == '__main__':
    lst = [[1, 2], [1, 3], [1, 4]]
    print(convert_fracts(lst))
