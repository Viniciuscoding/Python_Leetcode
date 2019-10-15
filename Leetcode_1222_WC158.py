"""
Queens That Can Attack the King

On an 8x8 chessboard, there can be multiple Black Queens and one White King.
Given an array of integer coordinates queens that represents the positions of the Black Queens, and a 
pair of coordinates king that represent the position of the White King, return the coordinates of all 
the queens (in any order) that can attack the King.


Example 1:

Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]
       king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],
                 [0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],
                 [1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],
                 [1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],
                 [0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
                 
       king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
 

Constraints:

1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
At most one piece is allowed in a cell.
"""

class Solution(object):
      def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
        # 1,2 |       1,4       | 1,6
        #       2,3 | 2,4 | 2,5
        # 3,2 | 3,3 | 3,4 | 3,5 | 3,6
        #       4,3 | 4,4 | 4,5
        # 5,2 |       5,4       | 5,6
        
        queen_hit = []
        dd_c, ii_c, kd_c, ki_c = True, True, True, True
        dk_c, ik_c, di_c, _id_c = True, True, True, True
        
        
        for i in range(8):
            # \  = decrease,decrease
            dd = [king[0] - i,king[1] - i]
            if dd in queens and dd_c:
                queen_hit.append(dd)
                dd_c = False
                print("dd = ", dd)
            # \  = increase,increase
            ii = [king[0] + i,king[1] + i]
            if ii in queens and ii_c:
                queen_hit.append(ii)
                ii_c = False
                print("ii = ", ii)
            #<-- = keep,decrease
            kd = [king[0],king[1] - i]
            if kd in queens and kd_c:
                queen_hit.append(kd)
                kd_c = False
                print("kd = ", kd)
            #--> = keep,increase
            ki = [king[0],king[1] + i]
            if ki in queens and ki_c: 
                queen_hit.append(ki)
                ki_c = False
                print("ki = ", ki)
            # |  = decrease,keep
            dk = [king[0]-i,king[1]]
            if dk in queens and dk_c: 
                queen_hit.append(dk)
                dk_c = False
                print("dk = ", dk)
            # |  = increase,keep
            ik = [king[0]+i,king[1]]
            if ik in queens and ik_c: 
                queen_hit.append(ik)
                ik_c = False
                print("ik = ", ik)
            # /  = decrease,increase
            di = [king[0] - i,king[1] + i]
            if di in queens and di_c:
                queen_hit.append(di)
                di_c = False
                print("di = ", di)
            # /  = increase,decrease
            _id = [king[0] + i,king[1] - i]
            if _id in queens and _id_c:
                queen_hit.append(_id)
                _id_c = False
                print("_id = ", _id)
      return queen_hit
