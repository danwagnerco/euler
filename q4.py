"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(num):
    forward = str(num)
    backward = str(num)[::-1]
    return forward == backward and forward != "0"

palindromes = []
for x in range(999, -1, -1):
    for y in range(999, -1, -1):
        if is_palindrome(x * y):
            palindromes.append(x * y)

print(max(palindromes))

