"""
Find All Strings with a Key Substring

Suppose you have an array of strings 'src' and a string 'key':

src = ["minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"]
key = "craft"

Now return all the strings from the 'src' array that contains the key as substring in them.
For example, for above case, the solution should be:

result = ["minecraftgame", innercrafttalent", "stonecrafter"]

Because all the result starings have key i.e. "craft" in them as substring
"""

def findSubString(self, src: List[str], key: str, words: List[str]) -> List[str]:
    return [words for words in src if key in words] 
