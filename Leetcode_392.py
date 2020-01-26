"""
Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000)
string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde"
while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its
subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # MY SOLUTION [VERY SLOW]
        tag = brek = 0
        
        print(enumerate(iter(t)))
        if len(s) == 0:
            return True
        
        for seq in s:
            while tag < len(t):
                if seq == t[tag]:
                    tag += 1
                    brek += 1
                    break
                else:
                    tag += 1
            if tag == len(t) and brek < len(s):
                return False
        return True
        
        # SOLUTION by AlgoGuruZ
        i = j = 0
        s_rng, t_rng = len(s), len(t)
        
        while i < s_rng and j < t_rng:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == s_rng

        # SOLUTION by StefanPochmann
        t = iter(t)
        return all(c in t for c in s)
        
        # [FASTEST!] SOLUTION by leetcode
        start = 0
        
        for c in s:
            i = t.find(c, start)
            if i == -1:
                return False
            start = i + 1
        return True
