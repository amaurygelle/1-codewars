'''
Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum

If there are two or more pairs with the required sum,
the pair whose second element has the smallest index is the solution
'''

def sum_pairs(ints, s):
    index_1 = None
    index_2 = None
    for i in range(len(ints)-1):
        j = 1
        while j < len(ints)-i:
            new_s = ints[i] + ints[i+j]
            if new_s == s and index_2 and index_2 > i+j:
                index_1 = i
                print(index_1)
                index_2 = i+j
                print(index_2)
            print(new_s)
            j += 1
    print('solution')
    print(ints[index_1], ints[index_2])
    return ints[index_1], ints[index_2] if index_1 and index_2 else None



if __name__ == '__main__':
    ints = [11, 3, 7, 5]
    s = 10

    sum_pairs(ints, s)
