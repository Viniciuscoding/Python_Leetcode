"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

# MY SOLUTION

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        min_i = min(map(lambda x: len(x), strs))
        
        first = strs[0]
        count = 0
        pf = ""
        
        for c in range(min_i):
            count = 0
            for word in strs:
                if first[c] == word[c]:
                    count += 1
                else:
                    break
            # count == len(strs) -> check if the character was found in all words
            # len(pf) == c -> check if the characters found are continuous by comparing the number of characters in pf with the index number before a character is added. If pf is smaller than the index a character was skipped, soon the prefix has been found if any character was added to pf.
            if count == len(strs) and len(pf) == c:
                pf += first[c]
            else:
                return pf  
        return pf    
