"""
Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # MY SOLUTION
        size = len(cost)
        distance = [0]*size
        distance[0], distance[1] = cost[0], cost[1]
        
        for i in range(2, size, 1):
            distance[i] = min(distance[i - 1] + cost[i], distance[i - 2] + cost[i]) 
        
        return min(distance[-1], distance[-2])
        
        # DP SOLUTION by Trickee
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost), 1):
            pre, cur = cur, min(pre, cur) + cost[i]
        return min(pre, cur)

        # DP SOLUTION by Leetcode
        r = [0] * len(cost)
        r[0], r[1] = cost[0], cost[1]
        for i in range(2, len(cost), 1):
            r[i] = cost[i] + min(r[i-1], r[i-2])
        return min(r[-1], r[-2])
