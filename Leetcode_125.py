"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
"""

class Solution(object):
    def isPalindrome(self, s):
        
        new_Pal = [c.lower() for c in s if c.isalnum()]

        return new_Pal == new_Pal[::-1]
        
# EXPLANATION

# Iterate through the string and remove any sign. Only keep letters from the alphabet and numbers.
# Return true or false if the array created via the iteratation is the same as its inverse array.
