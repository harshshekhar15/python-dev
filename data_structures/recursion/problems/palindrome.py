"""
Write a recursive function called isPalindrome which returns true if the string passed to it
is a palindrome (reads the same forward and backward). Otherwise it returns false.

Examples

isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
isPalindrome('amanaplanacanalpanama') # true
isPalindrome('amanaplanacanalpandemonium') # false
"""

def isPalindrome(strng):
    if len(strng) == 1:
        return True
    elif len(strng) == 2:
        return strng[0] == strng[1]
    else:
        return isPalindrome(strng[1:len(strng)-1]) and strng[0] == strng[len(strng)-1]

print(isPalindrome('amanaplanacanalpandemonium'))