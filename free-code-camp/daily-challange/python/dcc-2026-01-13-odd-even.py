"""Odd or Even?

Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.
Tests

Passed: 1. odd_or_even(1) should return "Odd".
Passed: 2. odd_or_even(2) should return "Even".
Passed: 3. odd_or_even(13) should return "Odd".
Passed: 4. odd_or_even(196) should return "Even".
Passed: 5. odd_or_even(123456789) should return "Odd"."""

def odd_or_even(n):

    return "Even" if n % 2 == 0 else "Odd" 

print(odd_or_even(1))