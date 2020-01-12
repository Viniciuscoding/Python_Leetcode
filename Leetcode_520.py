"""
Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    
    # My SOLUTION faster but a lot of code
        if len(word) == 1:
            return True
        else:
            for i in range(len(word)):
                #print(word[i])
                if ord(word[0]) - 97 < 0: # Capital
                    if ord(word[1]) - 97 >= 0: # Lowercase
                        if i > 1:
                            if ord(word[i]) - 97 >= 0: # Lowercase
                                continue
                            else: # Capital
                                return False
                        else:
                            continue

                    else: # Capital
                        if ord(word[i]) - 97 < 0: # Capital
                            continue
                        else: # Lowercase
                            return False
                else: # Lowercase
                    if ord(word[1]) - 97 < 0: # Capital
                        return False
                    else: # Lowercase
                        if i > 1:
                            if ord(word[i]) - 97 >= 0: # Lowercase
                                continue
                            else: # Capital
                                return False
                        else:
                            continue
        return True
# MY SOLUTION slower but less code
#         cC = []
#         for char in word:
#             if ord(char) - 97 >= 0:
#                 cC.append(0)
#             else:
#                 cC.append(1)
        
#         if cC[0] == 1 and sum(cC) == 1:
#             return True
#         elif sum(cC) == len(word):
#             return True
#         elif sum(cC) == 0:
#             return True
#         else:
#             return False
