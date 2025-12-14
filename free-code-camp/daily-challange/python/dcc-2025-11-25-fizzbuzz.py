# FizzBuzz
# Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

# 3 with "Fizz".
# 5 with "Buzz".
# 3 and 5 with "FizzBuzz".


def fizz_buzz(n):
    lst = []
    for l in list(range(1,n+1)):
        if l % 3 == 0 and l % 5 == 0:
            l = "FizzBuzz"
        elif l % 3 == 0:
            l = "Fizz"
        elif l % 5 == 0:
            l = "Buzz"
        lst.append(l)
    return lst
print(fizz_buzz(50))

