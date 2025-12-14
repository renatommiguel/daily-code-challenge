"""
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests
Passed:1. title_case("hello world") should return "Hello World".
Passed:2. title_case("the quick brown fox") should return "The Quick Brown Fox".
Passed:3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
Passed:4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
"""



def title_case(title):
    title = title.lower().split(" ")
    for ind,word in enumerate(title):
        title[ind] = word.title()
    title = " ".join(title)
    return title

if __name__ == "__main__":
    t = title_case("AvOcAdO tOAst fOr brEAkfAst")
    print(t)