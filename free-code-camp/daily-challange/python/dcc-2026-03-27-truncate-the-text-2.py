"""Truncate the Text 2

Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:
Letters 	Width
"ilI" 	1
"fjrt" 	2
"abcdeghkmnopqrstuvwxyzJL" 	3
"ABCDEFGHKMNOPQRSTUVWXYZ" 	4

The table above includes all upper and lower case letters. Additionally:

    Spaces (" ") have a width of 2

    Periods (".") have a width of 1

    If the given string is 50 units or less, return the string as-is, otherwise

    Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over.

Tests:

    Waiting: 1. truncate_text("The quick brown fox")             "The quick brown f..."
    Waiting: 2. truncate_text("The silky smooth sloth")            "The silky smooth sloth"
    Waiting: 3. truncate_text("THE LOUD BRIGHT BIRD")            "THE LOUD BRIG..."
    Waiting: 4. truncate_text("The fast striped zebra")            "The fast striped z..."
    Waiting: 5. truncate_text("The big black bear")           "The big black bear"
    """



def truncate_text(s):
    def get_w(c):
        lst1 = "ilI."
        lst2 = "fjrt "
        lst3 = "abcdeghkmnopqrstuvwxyzJL"
        lst4 = "ABCDEFGHKMNOPQRSTUVWXYZ"
        if c in lst1: return 1
        if c in lst2: return 2
        if c in lst3: return 3
        if c in lst4: return 4
        return 0

    if sum(get_w(c) for c in s) <= 50:
        print(s)
        return s
    
    ELLIPSIS = 3
    LIMIT = 50 - ELLIPSIS

    word = []
    count = 0

    for c in s:
        wc = get_w(c)
        if wc + count >= LIMIT:
            txt = "".join(word) + "..."
            print(txt)
            return txt
        word.append(c)
        count+=wc


if __name__ == "__main__":
    truncate_text("The quick brown fox")      
    truncate_text("The silky smooth sloth")   
    truncate_text("THE LOUD BRIGHT BIRD")     
    truncate_text("The fast striped zebra")   
    truncate_text("The big black bear")       







