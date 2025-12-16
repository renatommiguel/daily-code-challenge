"""
Consonant Count

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

    Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
    Ignore digits, punctuation, spaces, and other non-letter characters when counting.

Tests

has_consonant_count("helloworld", 7) should return True.
has_consonant_count("eieio", 5) should return False.
has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) should return False.
has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) should return True.
"""

def has_consonant_count(word:str, number:int) -> bool:
    count = 0
    for letter in word:
        if letter.isalpha():
            if letter not in 'aeiouAEIOU':
                count+=1
    print(count)
    return number == count

if __name__ == "__main__":
    has_consonant_count("helloworld", 7)
    has_consonant_count("eieio", 5)
    has_consonant_count("freeCodeCamp Rocks!", 11)
    has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24)
    has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23)
