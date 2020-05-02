"""
Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

# SOLUTION by yangshun
class Solution(object):
    def validPalindrome(self, s):
            
        front, back = 0, len(s) - 1
        
        while front < back:
            
            if s[front] != s[back]:
                beg, end = s[front:back], s[front + 1:back + 1]
                return beg == beg[::-1] or end == end[::-1]
            
            front, back = front + 1, back - 1
            
        return True

# EXPLANATION

# e.g. "aabbbbcaa"
#1 If the inverse of the string is not the same check if it is once one character is removed.
#2 There are two possible ways to remove a character. I call them beg and end.
# beg = means the character coming from the beginning character to one character before the end character in the array.
# In other words, beg is the substring withing brackets such as in this "aa[bbbb]caa"
# end = means the character comes from the ending character to one charater after the beginning character in the array.
# In other words, end is the substring withing brackets such as in this "aab[bbbc]aa"
#3 Check if the remaining array excluding the beg character is a palindrome or if the remaining array 
# excluding the end character is a palindrome
# For example "aabbbbcaa" the beg = "bbbb" and end = "bbbc". In this case beg is a palindrome.
