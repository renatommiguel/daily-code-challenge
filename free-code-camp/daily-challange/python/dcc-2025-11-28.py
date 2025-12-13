"""
Word Guesser
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").

Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests
compare("APPLE", "POPPA")# should return "10201".
compare("REACT", "TRACE")# should return "11221".
compare("DEBUGS", "PYTHON")# should return "000000".
compare("JAVASCRIPT", "TYPESCRIPT")# should return "0000222222".
compare("ORANGE", "ROUNDS")# should return "110200".
compare("WIRELESS", "ETHERNET")# should return "10021000".


"""

def compare(word, guess):
    print(f'--word:{word}----guess:{guess}----')
    if not isinstance(word,str):
        return False
    if not isinstance(guess,str):
        return False
    if not len(word) == len(guess):
        return False
    guess = guess.upper()
    word = word.upper()
    unique_letters = set(word)
    length = len(word)
    res = length * [0]
    dic = {l:{'wc':word.count(l), 'c':0, 'l':l} for l in list(unique_letters)}
    for ind, letter in enumerate(guess):
        if letter in unique_letters:
            if word[ind] == guess[ind]:
                print("a ",ind)
                print(dic[letter])

                dic[letter]['c'] = dic[letter]['c']+1
                print(dic[letter])

                res[ind]=2
    for ind, letter in enumerate(guess):
        if letter in unique_letters:
            if word[ind] != guess[ind]:
                if dic[letter]['wc'] > dic[letter]['c']:
                    print("b ",ind)
                    print(dic[letter])

                    dic[letter]['c'] = dic[letter]['c']+1
                    print(dic[letter])
                    res[ind]=1
    w = ''
    for x in res:
        w = w+str(x)
    print(w)
    return w
if __name__ == "__main__":
    compare("APPLE", "POPPA")# should return "10201".
    compare("REACT", "TRACE")# should return "11221".
    compare("DEBUGS", "PYTHON")# should return "000000".
    compare("JAVASCRIPT", "TYPESCRIPT")# should return "0000222222".
    compare("ORANGE", "ROUNDS")# should return "110200".
    compare("WIRELESS", "ETHERNET")# should return "10021000".