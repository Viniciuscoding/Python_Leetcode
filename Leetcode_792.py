"""
Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example 1:
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

# MY SOLUTION
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        countSeq = 0
        for word in words:
            if isSequence(word, S):
                 countSeq += 1
        return countSeq
    
def isSequence(s: str, t: str) -> bool:
    start = 0
        
    for c in s:
        i = t.find(c, start)
        if i == -1:
            return False
        start = i + 1
    return True
