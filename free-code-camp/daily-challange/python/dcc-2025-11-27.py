"""
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.
Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests
calculate_age("2000-11-20") # should return 25.
calculate_age("2000-12-01") # should return 24.
calculate_age("2014-10-25") # should return 11.
calculate_age("1994-01-06") # should return 31.
calculate_age("1994-12-14") # should return 30.
"""
def calculate_age(birthday):
    b = birthday.split('-')
    y = 2025 - int(b[0])
    m = 11 - int(b[1])
    d = 27 - int(b[2])
    if m<0 or d<0:
        y = y-1
    print(y)
    return y

if __name__ == "__main__": 
    calculate_age("2000-11-20") # should return 25.
    calculate_age("2000-12-01") # should return 24.
    calculate_age("2014-10-25") # should return 11.
    calculate_age("1994-01-06") # should return 31.
    calculate_age("1994-12-14") # should return 30.