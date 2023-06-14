import numpy as np
from math import prod

def convert_fracts(lst):
    denominator = int(prod([i[1] for i in lst]))
    print(denominator)
    numerator = int(sum([i[0]*denominator/i[1] for i in lst]))
    print(numerator)
    gcd = np.gcd(numerator, denominator)
    den_final = int(denominator / gcd)
    print(den_final)
    return [[int(i[0]*den_final/i[1]), den_final] for i in lst]


if __name__ == '__main__':
    lst = [[1, 2], [1, 3], [1, 4]]

    a = 98
    b = 42
    c = 14
    gcd = np.gcd.reduce([a, b, c])
    print(f'{a}/{b} == {int(a/gcd)}/{int(b/gcd)}')
    print(convert_fracts(lst))
