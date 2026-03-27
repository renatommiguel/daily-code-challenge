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

if __name__ == "__main__":
    truncate_text("The quick brown fox")      
    truncate_text("The silky smooth sloth")   
    truncate_text("THE LOUD BRIGHT BIRD")     
    truncate_text("The fast striped zebra")   
    truncate_text("The big black bear")       

    truncate_text("The quick brown f...")
    truncate_text("The silky smooth sloth")
    truncate_text("THE LOUD BRIG...")
    truncate_text("The fast striped z...")
    truncate_text("The big black bear")






# truncate_text("The quick brown fox")  
# truncate_text("The quick brown f...")


# truncate_text("The silky smooth sloth")   
# truncate_text("The silky smooth sloth")

# truncate_text("THE LOUD BRIGHT BIRD")  
# truncate_text("THE LOUD BRIG...")

truncate_text("The fast striped zebra")
truncate_text("The fast striped z...")

# truncate_text("The big black bear") 
# truncate_text("The big black bear")


