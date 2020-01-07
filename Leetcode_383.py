"""
Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # MY SOLUTION (Faster)
        r = 0
        while r < len(ransomNote):
            if ransomNote[r] not in magazine:
                return False
            else:
                magazine = magazine.replace(ransomNote[r], '', 1)
                r += 1   
        return True
        
#        SOLUTION by Xiaolong
#         arr = [0]*26

#         for m in magazine:
#             arr[ord(m) - 97] += 1
#         for r in ransomNote:
#             arr[ord(r) - 97] -= 1
#             if arr[ord(r) - 97] < 0:
#                 return False
#         return True
