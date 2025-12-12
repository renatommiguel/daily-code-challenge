"""
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.



Tests
parse_bold("**This is bold**") should return "<b>This is bold</b>".
parse_bold("__This is also bold__") should return "<b>This is also bold</b>".
parse_bold("**This is not bold **") should return "**This is not bold **".
parse_bold("__ This is also not bold__") should return "__ This is also not bold__".
parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.") should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.".

"""    

def parse_bold(val):
    if not ("__" in val or "**" in val):
        return val
    md = val.split()
    lst = []
    for word in md:
        if ((word.startswith("**") and word.endswith("**")) or (word.startswith("__") and word.endswith("__"))) and len(word)>4:
            w=word[2:-2]
            lst.append(f"<b>{w}</b>")
        elif (word.startswith("**") or word.startswith("__") ) and len(word)>2:
            w=word[2:]
            lst.append(f"<b>{w}")
        elif (word.endswith("**") or word.endswith("__") ) and len(word)>2:
            w=word[:-2]
            lst.append(f"{w}</b>")
        else:
            lst.append(word)
    res = " ".join(lst)
    if "**" in lst or "__" in lst:
        res = val    
    return res

if __name__ == "__main__":
    parse_bold("**This is bold**") 
    parse_bold("__This is also bold__") 
    parse_bold("**This is not bold **") 
    parse_bold("__ This is also not bold__") 
    parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")