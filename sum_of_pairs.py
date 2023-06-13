'''
Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum

If there are two or more pairs with the required sum,
the pair whose second element has the smallest index is the solution
'''

def sum_pairs(ints, s):
    index_1 = None
    index_2 = None
    old_index_2 = 1000
    for i in range(len(ints)-1):
        j = 1
        while j < len(ints)-i:
            new_s = ints[i] + ints[i+j]
            if new_s == s:
                index_1 = i if i+j < old_index_2 else index_1
                index_2 = i+j if i+j < old_index_2 else index_2
                old_index_2 = index_2
            j += 1
    return [ints[index_1], ints[index_2]] if index_1 != None and index_2 != None else None



if __name__ == '__main__':
    ints = [11, 3, 7, 5]
    s = 10

    ints = [4, 3, 2, 3, 4]
    s = 6

    ints = [4, 3, 2, 3, 4]
    s = 2

    ints = [20, -13, 40]
    s = -7

    print(sum_pairs(ints, s))
