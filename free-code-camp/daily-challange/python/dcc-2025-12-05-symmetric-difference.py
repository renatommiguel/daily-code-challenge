"""
symmetric difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.

1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
Waiting:2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
Waiting:3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
Waiting:4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
"""

def difference(arr1, arr2):
    arr = []
    for i in arr1:
        if i not in arr2:
            arr.append(i)
    for i in arr2:
        if (i not in arr1) and (i not in arr):
            arr.append(i)  
    print(arr)
    return arr
difference([1, 2, 3], [3, 4, 5])