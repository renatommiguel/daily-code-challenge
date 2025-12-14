"""BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.
"""


def is_fizz_buzz(seq):
    flag = False
    lst = list(range(1,len(seq)+1))
    for ind,el in enumerate(lst):
        if el%15==0:
            lst[ind] = "FizzBuzz"
        elif el%5==0:
            lst[ind] = "Buzz"
            True
        elif el%3==0:
            lst[ind] = "Fizz"
            True
    print(lst)
    return seq==lst

    

if __name__ == '__main__':
    lst = [1, 2, "Fizz", 4]
    print(is_fizz_buzz(lst))
    lst = [1, 2, 3, 4]
    print(is_fizz_buzz(lst))
