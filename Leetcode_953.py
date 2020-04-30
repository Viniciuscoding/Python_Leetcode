"""
Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical
rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character 
(More info).
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashit = {val: i for i, val in enumerate(order)}
        
        word_2_num = []
        
        for word in words:
            nums = []
            for c in word:
                nums.append(hashit[c])
                
            word_2_num.append(nums)

        for w2num, next_w2num in zip(word_2_num, word_2_num[1:]):
            if w2num > next_w2num:
                return False
        
        return True

       
 # EXPLANATION
 
 #1. Create a dictionary out or order array with key the letter and index the value.
 #2. Change the words' characters to the dictionary's respective values.
 #3. Use zip() to check if every character in the first word is not greater than the following words characters.
 #4. If all the words falls under the #3 if statement then return True.
