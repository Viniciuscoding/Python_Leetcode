/*
Hexspeak

A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, 
then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I. Such a representation is 
valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise
return "ERROR".

Example 1:

Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.

Example 2:

Input: num = "3"
Output: "ERROR"
 
Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.
*/

class Solution:
    def toHexspeak(self, num: str) -> str:
        hexspeak = ""
        remainder = 0
        num = int(num)
        while num > 0:
            remainder = num % 16
            if remainder == 0:
                hexspeak += 'O'
            elif remainder == 1:
                hexspeak += 'I'
            elif remainder == 10:
                hexspeak += 'A'
            elif remainder == 11:
                hexspeak += 'B'
            elif remainder == 12:
                hexspeak += 'C'
            elif remainder == 13:
                hexspeak += 'D'
            elif remainder == 14:
                hexspeak += 'E'
            elif remainder == 15:
                hexspeak += 'F'
            else:
                return "ERROR"
            num = num // 16
        return hexspeak[::-1]
