"""
Roman Numeral Builder
Given an integer, return its equivalent value in Roman numerals.

Roman numerals use these symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).



Waiting:1. to_roman(18) should return "XVIII".
Waiting:2. to_roman(19) should return "XIX".
Waiting:3. to_roman(1464) should return "MCDLXIV".
Waiting:4. to_roman(2025) should return "MMXXV".
Waiting:5. to_roman(3999) should return "MMMCMXCIX".

"""
def to_roman(num):
    # break into 1000, 100, 10, 1
    m  = num//1000
    r1 = num%1000

    c =  r1//100
    r2 = r1%100
    
    x  =  r2//10
    r3 = r2%10
    
    i  =  r3//1
    r4 = r3%1
    res = ""
    def calc(val,low,mid,high):
        if val <= 3:
            res = val*low
        elif val == 4:
            res = low+mid
        elif val == 5:
            res = mid
        elif 5 < val < 9:
            res = mid+(val-5)*low
        elif val==9:
            res = low+high
        return res
    resm = m*"M"
    resc = calc(c,"C","D","M")
    resx = calc(x,"X","L","C")
    resi = calc(i,"I","V","X")
    res = resm + resc+resx+resi
    return res

if __name__ == "__main__":
    
    def to_roman_copilot(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

    # # Test cases
    print(to_roman(18))    # Should return "XVIII"
    print(to_roman(19))    # Should return "XIX"
    print(to_roman(1464))  # Should return "MCDLXIV"
    print(to_roman(2025))  # Should return "MMXXV"
    print(to_roman(3999))  # Should return "MMMCMXCIX"