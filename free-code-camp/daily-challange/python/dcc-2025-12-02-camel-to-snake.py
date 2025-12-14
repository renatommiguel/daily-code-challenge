"""
camel to snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).


Tests
Waiting:1. to_snake("helloWorld") should return "hello_world".
Waiting:2. to_snake("myVariableName") should return "my_variable_name".
Waiting:3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
"""

def to_snake(camel):
    res = []
    lst = [l for l in camel]
    if not lst[0].islower():
        return "Not camelCase"
    for i,l in enumerate(lst):
        if l.isupper():
            res.append("_")
            res.append(l.lower())
        else:
            res.append(l)
    res = "".join(res)
    return res

to_snake("helloWorld") #should return "hello_world".
to_snake("myVariableName") #should return "my_variable_name".
to_snake("freecodecampDailyChallenges") #should return "freecodecamp_daily_challenges".