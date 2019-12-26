"""
Remove Vowels from a String


Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 
Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""

import re

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        # MY SOLUTION
        return "".join(re.findall(r'[^aeiou]', S))
        
        # SOLUTION by @721
        return re.sub('a|e|i|o|u', '', S)
    
        # SOLUTION by lee215
        return "".join(c for c in S if c not in "aeiou")

