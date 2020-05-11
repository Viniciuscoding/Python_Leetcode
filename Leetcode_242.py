"""
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution(object):
    def isAnagram(self, s, t):
       # SOLUTION slower
        s_c = Counter(s)
        t_c = Counter(t)
        
        return s_c == t_c

       # SOLUTION fastest  
        st = set(s + t)
        for c in st:
            if s.count(c) != t.count(c):
                return False
            
        return True
