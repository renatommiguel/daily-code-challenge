"""
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
"""
def compress_string(sentence):
    sentence_split = sentence.split(" ")
    uniq_words = list(dict.fromkeys(sentence_split))
    res = ""
    length = len(uniq_words)
    for ind,word in enumerate(uniq_words):
        count_word = sentence_split.count(word)
        if count_word > 1:
            res+=f"{word}({count_word}) "
        else:
            res+=f"{word} "
        # if ind+1 < length:
        #     res+=" "
    res = res.strip()
    print(res)
    return res


compress_string("yes yes yes please")
compress_string("I have have have apples")
compress_string("one one three and to the the the the")
compress_string("route route route route route route tee tee tee tee tee tee")

