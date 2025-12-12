"""
Most Frequent

Given an array of elements, return the element that appears most frequently.

    There will always be a single most frequent element.


Tests

Waiting: 1. most_frequent(["a", "b", "a", "c"]) should return "a".
Waiting: 2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
Waiting: 3. most_frequent([True, False, "False", "True", False]) should return False.
Waiting: 4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 


"""


def most_frequent(arr):
    dic = {}
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    mf = max(dic.values())
    for k,v in dic.items():
        if v ==mf:
            return k
    return arr



if __name__ == '__main__':

    most_frequent(["a", "b", "a", "c"])  
    most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) 
    most_frequent([True, False, "False", "True", False]) 
    most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60])

