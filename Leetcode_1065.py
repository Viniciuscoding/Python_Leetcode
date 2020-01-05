"""
Index Pairs of a String

Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] 
is in the list of words.

Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
 

Note:
All strings contains only lowercase English letters.
It's guaranteed that all strings in words are different.

1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50

Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their
second coordinate).
"""

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # COULD NOT SOLVE IT!!
#         ls_words = []
#         w = 0
                
#         for word in words:
#             w = text.find(word)
#             ls_words.append([w, w + len(word) - 1])
#         ls_words.sort()   
#         return [[i,j] for i,j in ls_words]
    
        # SOLUTION by mrjerryho
        res = []
        for word in words:
            i = text.find(word)
            while i != -1:
                res.append([i, i+len(word)-1])
                i = text.find(word, i+1)
        res.sort()
        return res
