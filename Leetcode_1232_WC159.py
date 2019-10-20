"""
Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

class Solution(object):
    def checkStraightLine(self, coordinates):
        slope, prev_slope = 0, -1
        i, j = 0, 1
        
        while j < len(coordinates):
            if prev_slope != -1:
                if (coordinates[j][0] - coordinates[i][0]) == 0:
                    slope = 0
                    if prev_slope == slope:
                        prev_slope = slope
                    else:
                        return False
                    j += 1
                    i += 1
                else:
                    slope = (coordinates[j][1] - coordinates[i][1]) / (coordinates[j][0] - coordinates[i][0])
                    if prev_slope == slope:
                        prev_slope = slope
                    else:
                        return False
                    j += 1
                    i += 1
            else:
                if (coordinates[j][0] - coordinates[i][0]) == 0:
                    slope = 0
                    prev_slope = slope
                    j += 1
                    i += 1
                else:
                    slope = (coordinates[j][1] - coordinates[i][1]) / (coordinates[j][0] - coordinates[i][0])
                    prev_slope = slope
                    j += 1
                    i += 1
        return True


