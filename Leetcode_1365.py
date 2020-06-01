"""
How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        # MY SOLUTION fastest
        snums = sorted(nums)
        counted = {}
        
        for i in range(len(snums)):
            if snums[i] not in counted:
                counted[snums[i]] = i
        return [counted[n] for n in nums]
class Solution2(object):
   def smallerNumbersThanCurrent(self, nums):
        
        # MY SOLUTION 2nd fastest
        unums = set(nums)
        dic = {}
        
        for num in unums:
            if num not in dic:
                for i in range(len(nums)):
                    if num != nums[i] and num > nums[i]:
                        count += 1
                dic[num] = count
                count = 0
        return [dic[n] for n in nums]
     
class Solution3(object):
   def smallerNumbersThanCurrent(self, nums):        
    
        # MY SOLUTION slowest
        count = 0
        output = []
        
        for num in nums:
            for i in range(len(nums)):
                if num != nums[i] and num > nums[i]:
                    count += 1
            output.append(count)
            count = 0
        return output


