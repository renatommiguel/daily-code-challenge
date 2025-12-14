"""
Markdown Ordered List Item Converter
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.



Tests
Waiting:1. convert_list_item("1. My item") should return "<li>My item</li>".
Waiting:2. convert_list_item(" 1.  Another item") should return "<li>Another item</li>".
Waiting:3. convert_list_item("1 . invalid item") should return "Invalid format".
Waiting:4. convert_list_item("2. list item text") should return "<li>list item text</li>".
Waiting:5. convert_list_item(". invalid again") should return "Invalid format".
Waiting:6. convert_list_item("A. last invalid") should return "Invalid format".
"""




def convert_list_item(val):
    lst_no_space = val.split()
    if "." in lst_no_space[0]:
        if lst_no_space[0][0].isnumeric():
            return to_html(" ".join(val.split()[1:]))
        else:
            return invalid()
    else:
        return invalid()

    return val

def to_html(text):
    return f"<li>{text}</li>"
def invalid():
    return "Invalid format"


convert_list_item("1. My item") #should return "<li>My item</li>".
convert_list_item(" 1.  Another item") #should return "<li>Another item</li>".
convert_list_item("2. list item text")# should return "<li>list item text</li>".

convert_list_item(". invalid again") # should return "Invalid format".
convert_list_item("A. last invalid")  #should return "Invalid format".
convert_list_item("1 . invalid item")# should return "Invalid format".
