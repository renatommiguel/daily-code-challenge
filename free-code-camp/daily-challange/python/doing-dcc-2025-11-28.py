def compare(word, guess):
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
    dic = {l:{'wc':word.count(l), 'gc':0,'l':l} for l in list(set(word))}
    new_word=""
    for ind, letter in enumerate(guess):
        if letter in word:
            if word[ind] == guess[ind]:
                dic[letter]['gc']+=+1
                res[ind]=2

                
    for ind, letter in enumerate(guess):
        if letter in word:
            dic[letter]['gc'] = dic[letter]['gc']+1
            if not dic[letter]['gc']>2 and res[ind]!=2:
                    res[ind]=1

    # x = {l:{'count':word.count(l),"first_index":word.index(l)} for l in list(set(word))}
    w = ''
    for x in res:
        w = w+str(x)
    print(w)
    return w
if __name__ == '__main__':

    compare("JAVASCRIPT", "TYPESCRIPT")
