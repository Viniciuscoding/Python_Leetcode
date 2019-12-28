"""
Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # hello          holle
        # 01234          04231
        #  1  4  vowels   4  1
        
        # leetcode       leotcede
        # 01234567       07534261
        #  12  5 7 vowels 75  2 1
        
        # MY SOLUTION
        vowels = "aeiouAEIOU"
        s_ls = list(s)
        v_ind = []
        s_L = len(s)
        
        for i in range(s_L):
            if s_ls[i] in vowels:
                s_ls[i] = '~'
                v_ind.append(i)
            else:
                continue
                
        v_L = len(v_ind) - 1
        
        for f in range(s_L):
            if s_ls[f] == '~':
                s_ls[f] = s[v_ind[v_L]]
                v_L -= 1
            if v_L < 0:
                break
        
        return "".join(s_ls)                
