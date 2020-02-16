"""
Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""

# MY SOLUTION
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """        
        lengh_sum = 0
        chars_dic = {}
        
        for char in chars:
            chars_dic[char] = chars_dic.get(char,0) + 1
            
        for word in words:
            check = True
            for w in word:
                #if word.count(w) > chars.count(w):
                if word.count(w) > chars_dic.get(w,0):
                    check = False
                    break
            if check:
                lengh_sum += len(word)
                
        return lengh_sum

# SOLUTION hashmaping every word from words is slower
class Solution(object):
    def countCharacters(self, words, chars):
        check = False
        length_sum = 0
        
        char_dic = self.hashmap(chars)
        
        for word in words:
            check = True
            word_dic = self.hashmap(word)
            for key, value in word_dic.items():
                if key in char_dic:
                    if value > char_dic[key]:
                        check = False
                        break
                else:
                    check = False
                    break
            if check:
                length_sum += len(word)
                
        return length_sum
        
    def hashmap(self, word_here):
        chars_dic = {}
        
        # Shorter way to hashmap string's characters frequency
        for c in word_here:
            chars_dic[c] = chars_dic.get(c,0) + 1
        
        # for c in word_here:
        #     if c in chars_dic:
        #         chars_dic[c] += 1
        #     else:
        #         chars_dic[c] = 1
        
        return chars_dic
