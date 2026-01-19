"""
Free Shipping

Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

The given array will contain items from the list below:
Item 	Price
"shirt" 	34.25
"jeans" 	48.50
"shoes" 	75.00
"hat" 	19.95
"socks" 	15.00
"jacket" 	109.95
Tests

    Waiting: 1. gets_free_shipping(["shoes"], 50) should return True.
    Waiting: 2. gets_free_shipping(["hat", "socks"], 50) should return False.
    Waiting: 3. gets_free_shipping(["jeans", "shirt", "jacket"], 75) should return True.
    Waiting: 4. gets_free_shipping(["socks", "socks", "hat"], 75) should return False.
    Waiting: 5. gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100) should return True.
    Waiting: 6. gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200) should return False.
"""

def gets_free_shipping(cart, minimum):
    prices = {"shirt" 	:34.25,
            "jeans" 	:48.50,
            "shoes" 	:75.00,
            "hat" 	:19.95,
            "socks" 	:15.00,
            "jacket" 	:109.95,
            }   
    ammount = 0
    for elem in cart:
        if elem in prices.keys():
            ammount += prices[elem]
    return ammount > minimum

gets_free_shipping(["shoes"], 50) 
gets_free_shipping(["hat", "socks"], 50) 
gets_free_shipping(["jeans", "shirt", "jacket"], 75) 

gets_free_shipping(["socks", "socks", "hat"], 75) 
gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100) 
gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200) 