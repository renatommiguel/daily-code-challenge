"""
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

Waiting:1. count_permutations("abb") should return 3.
Waiting:2. count_permutations("abc") should return 6.
Waiting:3. count_permutations("racecar") should return 630.
Waiting:4. count_permutations("freecodecamp") should return 39916800.
"""




def count_permutations(s):
    lt = len(s)
    uniq = list(dict.fromkeys(s))
    # make a dictionary with the unique values and the amount of times they repeat
    # dic = {u:s.count(u) for u in uniq}
    #make a list of the uniq values and the factorial of the amount of times they repeat
    uf = [fac(s.count(u)) for u in uniq]
    den = 1
    for u in uf:
        den*=u
    res = fac(lt)/den 

    print(res)
    return res
def fac(v):
    if v==0:
        return 1
    if v<0:
        return "\nValueError: There is no factorial of negative numbers"
    res = 1
    for i in range(1,v+1):
        res*=i
    return res

count_permutations("racecar") 



# help from gemini 

# This is a classic problem that can be solved using a formula from 
# combinatorics (the mathematics of counting).The concept you need to 
# understand is how to find the number of distinct permutations when you 
# have a set of objects (characters) where some are identical (repeated).
# Here is the explanation, the formula, and how to apply it to your example.🔢 
# The Core Concept: Distinct PermutationsA permutation is an arrangement of all 
# the members of a set into some sequence or order.When all characters in a 
# string are unique (like in "abc"), the total number of permutations is simply 
# the factorial of the string's length, denoted as $n!$.For "abc" (length $n=3$), t
# he permutations are $3! = 3 \times 2 \times 1 = 6$.However, when a string has repeated characters (like in "abb"), 
# simply calculating $n!$ will overcount the distinct permutations because swapping two identical characters results 
# in the exact same arrangement, which shouldn't be counted twice.The Problem of OvercountingConsider your example, 
# "abb" (length $n=3$):If we treat the two 'b's as distinct, say $b_1$ and $b_2$, 
# the arrangements would be:$a b_1 b_2$$a b_2 b_1$$b_1 a b_2$$b_2 a b_1$$b_1 b_2 a$$b_2 b_1 a$In reality, 
# since $b_1 = b_2 = 'b'$, arrangements (1) and (2) are both just "abb", (3) and (4) are both "bab", and (5) and (6) 
# are both "bba".The factor by which we overcounted is exactly the number of ways we can arrange the identical characters
#  among themselves. Since there are two 'b's, there are $2! = 2$ ways to arrange them, so we overcounted by a factor of 2.T
#  he FormulaTo correct for this overcounting, we divide the total number of permutations (if all characters were unique, $n!$) 
#  by the factorial of the count for each unique, repeated character.
#  The formula for the number of distinct permutations is:$$\text{Distinct Permutations} = 
#  \frac{n!}{r_1! \cdot r_2! \cdot \ldots \cdot r_k!}$$Where:$n$ is the total number of characters in 
#  the string (the string's length).$r_1, r_2, \ldots, r_k$ are the counts (frequencies) of each repeated character. 
#  You must include the counts of all unique characters, even if they only appear once (since $1! = 1$, they don't 
#  change the division).