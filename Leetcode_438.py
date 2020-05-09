"""
Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution(object):
    def findAnagrams(self, s, p):

        p_size = len(p)
        s_list = list(s)
        p_list = list(p)
        p_list.sort()
        ar = []
        
        # FIRST SOLUTION CAN'T PASS TIME LIMIT
        
        for i in range(len(s) - p_size + 1):
            rang = s_list[i:(i+p_size)]
            rang.sort()
            if rang == p_list:
                ar.append(i)
            
        return ar

        # SECOND SOLUTION PASSES TIME LIMIT
        
        pDic = collections.Counter(p)
        sDic = collections.Counter(s[:len(p)])
        
        beg, end = 0, len(p)
        indexes = [] 
        
        while end <= len(s):
            if sDic == pDic:
                indexes.append(beg)
                
            sDic[s[beg]] -= 1
            
            if sDic[s[beg]] <= 0:
                sDic.pop(s[beg]) 
                
            if end < len(s):    
                sDic[s[end]] += 1
            
            end += 1
            beg += 1
        return indexes
        
# EXPLANATION
# 1. Create a dictionary of p with each character as key and their count as value.
# 2. Create a dictionary of s with each character as key and their count as value with the initial size range of p.
# 3. Create the range we will work with p and s to check if they are an anagram. Note, s range has to have the same size as p
#    The initial lower bound of the range is called "beg" and it starts at 0.
#    The initial upper bound of the range is called "end" and it starts at an index equal to the length of p.
# 4. Create a while loop and break it once end is bigger than the length of s.
#    NOTE: This loop help the dictionary to remove the lower bound character and move to the next character from the upper bound.
# 5. Check if each dictionary is the same. If they are, add beg to an empty array that was called "indexes". 
# 6. Decrement the value of the character from the character in the string s whose index is equal to the character at beg index.
# 7. Check if the character value of the character at beg index is equal to 0. If it is, pop that value from the dictionary.
$ 8. Add the next value character at the end index and increment its value by 1 to the dictionary. 
# of the size o string lenght of p which we call the "end" index.
# 9. Increment the beg and end by one each.
# 10. Loop through it until end is greater than the length of s than return indexes.
