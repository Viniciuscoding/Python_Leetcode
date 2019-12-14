"""
Unique Morse Code Words

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        CODE = [".-", "-...", "-.-.", "-..", ".", 
                "..-.", "--.", "....", "..", 
                ".---", "-.-", ".-..", 
                "--", "-.", "---", 
                ".--.", "--.-", 
                ".-.", "...", 
                "-", "..-", 
                "...-", 
                ".--", "-..-", "-.--", "--.."]
        
        # SOLUTION 1
        return len({''.join(CODE[ord(n) - ord('a')] for n in w) for w in words})
        
        # SOLUTION 2
        morse = ""
        m_code = []
        
        for i1 in range(len(words)):
            for i2 in range(len(words[i1])):
                i3 =  ord(words[i1][i2]) - ord('a')
                morse = morse + code[i3]
            m_code.append(morse)
            morse = ""
        return len(set(m_code))
    
