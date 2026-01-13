"""
Par for the Hole

Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

    "Hole in one!" if it took one stroke.
    "Eagle" if it took two strokes less than par.
    "Birdie" if it took one stroke less than par.
    "Par" if it took the same number of strokes as par.
    "Bogey" if it took one stroke more than par.
    "Double bogey" if took two strokes more than par.

Tests

Failed: 1. golf_score(3, 3) should return "Par"
Failed: 2. golf_score(4, 3) should return "Birdie"
Passed: 3. golf_score(3, 1) should return "Hole in one!"
Passed: 4. golf_score(5, 7) should return "Double bogey"
Failed: 5. golf_score(4, 5) should return "Bogey"
Failed: 6. golf_score(5, 3) should return "Eagle"
"""

def golf_score(par, strokes):
    gdic = {
    "Hole in one!" :1,
    "Eagle" :par-2,
    "Birdie" :par-1,
    "Par" :par,
    "Bogey" :par+1,
    "Double bogey" :par+2,
    }
    # print(gdic.items())
    for key,val in gdic.items():
        if val==strokes:
            return key
    return "Double bogey"

golf_score(3, 3)
# golf_score(4, 3)
# golf_score(3, 1)
# golf_score(5, 7)
# golf_score(4, 5)
# golf_score(5, 3)

