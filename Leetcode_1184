A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring 
stops where distance[i] is the distance between the stops number i and (i + 1) % n. The bus goes along both directions 
i.e. clockwise and counterclockwise. Return the shortest distance between the given start and destination stops.

Example 1:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.


Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        short_dist_asc, short_dist_asc= 0, 0
        all_dist = sum(distance)
        
        if start > destination:
            start, destination = destination, start
        for i in range(start,destination,1):
            short_dist_asc += distance[i] 
            print("i foward distance ",i," ", short_dist_asc)
        
        short_dist_des = all_dist - short_dist_asc
        
        return min(short_dist_asc,short_dist_des)
