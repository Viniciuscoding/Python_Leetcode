"""
Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
            
        # REPLACE() SOLUTION
        return address.replace(".", "[.]")
        
        # LIST SOLUTION
        # add_arr = list(address)
        # for i in range(len(address)):
        #     if add_arr[i] == ".":
        #         add_arr[i] = "[.]"
        #     else:
        #         continue
        # return "".join(add_arr)
