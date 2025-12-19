
"""
Pairwise

Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

    2 and 8 (2 + 8 = 10), whose indices are 0 and 4
    4 and 6 (4 + 6 = 10), whose indices are 2 and 3

Add all the indices together to get a return value of 9.
Tests

Passed: 1. pairwise([2, 3, 4, 6, 8], 10) should return 9.
Passed: 2. pairwise([4, 1, 5, 2, 6, 3], 7) should return 15.
Passed: 3. pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) should return 22.
Passed: 4. pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) should return 10.

"""




def pairwise(arr:list, target:int) -> int:
    res = []
    for ind1,ele1 in enumerate(arr):
            for ind2,ele2 in enumerate(arr):
                if ind1 != ind2:
                    if ele1 + ele2 == target:
                        res.append(ind1)
                        res.append(ind2)
    return sum(set(res))

if __name__ == "__main__":
    pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20)   