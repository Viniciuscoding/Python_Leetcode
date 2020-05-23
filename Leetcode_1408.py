"""
String Matching in an Array

Given an array of string words. Return all strings in words which is substring of another word in any order. 
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j]. 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""

class Solution(object):
    def stringMatching(self, words):
        
        # MY SOLUTION
        count = 0
        substr = []
        
        for w in words:
            for i in range(len(words)):
                #print("{} == {} is {}".format(w, words[i], w in words[i]))
                if w in words[i]:
                    count += 1
                if count >= 2:
                    substr.append(w)
                    count = 0
                    break
            count = 0
        return substr
        
        # SOLUTION by nterpsec
        full = ' '.join(words)
        return [w for w in words if full.count(w) >= 2]
