"""
K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
   
        # Euclidean Distance Formula
        # d = ((x2 - x1)^2 + (y2 - y1)^2)^(1/2)
        
        # MY SOLUTION
        d = 0
        d_list = {}
        d_ans = []
        
        for point in points:
            d = (point[0]**2 + point[1]**2)
            d_list[str(point)] = d
            
        sort_d_list = sorted(d_list.items(),  key = lambda x: x[1])[:K]

        for i in range(K):
            d_ans.append(eval(sort_d_list[i][0]))

        return d_ans
    
        # SOLUTION by lee215 (using heap queue function)
        #return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])
        
# EXPLANATION
# 1. Create a dictionary with coordinates as keys and distance of the coordinates to the origin as values.
# NOTE: dicitonary does not accept list type as keys so it is necessary to change the coordinates to string type
# Why? Because if distance results are keys the multiple distances with different coordinates but same distances
# will show only one distance beacause the dictionary only keeps unique keys.
# 2. Distance is calculated using the euclidean distance formula.
# 3. Sort the dictionary on ascending order by values. Lambda function is necessary to sort by values.
# 4. Loop through K range and change the coordinates from string types back to list types to store in an array. Ignore values.
