from typing import List

"""
Problem 1769: Min Number of Operations to Move All Balls to Each Box

You have n boxes. You are given a binary string boxes of length n, where 
boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball. 
In one operation, you can move one ball from a box to an adjacent box. Box i
is adjacent to box j if abs(i-j) == 1. Note that after doing so, there may be 
more than one ball in some boxes. Return an array answer of size n where 
answer[i] is the min number of operations needed to move all the balls to the
ith box.

Approach: Could do nested search where you calculate the distance away from i 
but somewhat inefficient. Intuition that all balls to the left of box i each 
need to move 1 more unit right in addition to any movements for i-1 and vice 
versa. 4 arrays, 2 to count how many ball detected boxes are to the left/right 
of i and 2 arrays to accumulate the left/right movements. Two linear searches 
are enough to count each side, determine left/right movements needed, and sum
movements to compute the solution. 


(nested search)
Runtime: 5608 ms, faster than 33.33%
Space: 14.5 MB, less than 100%
Runtime Complexity: O(N^2)
Space Complexity: O(N) (only to output soln matrix)

(dynamic programming)
Runtime: 80 ms, faster than 100%
Space: 14.8 MB, less than 33%
Runtime Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nestedSearchMinOperations(boxes):
        N = len(boxes)
        soln = [0]*N
        for i in range(N):
            sum_movements = 0
            for j in range(N):
                if boxes[j] == '1':
                    sum_movements += abs(j-i)
            soln[i] = sum_movements
        return soln

    def DPMinOperations(boxes):
        N = len(boxes)
        left_ones_count = [0]*N
        right_ones_count = [0]*N
        L = [0]*N
        R = [0]*N
        soln = [0]*N
        for i in range(1,N):
            is_ball_in_box = 1 if boxes[i-1] == '1' else 0
            left_ones_count[i] = left_ones_count[i-1] + is_ball_in_box
            L[i] = L[i-1] + left_ones_count[i]
        # print(L)
        for i in range(N-1, -1, -1):
            if i < N-1:
                is_ball_in_box = 1 if boxes[i+1] == '1' else 0
                right_ones_count[i] = right_ones_count[i+1] + is_ball_in_box
                R[i] = R[i+1] + right_ones_count[i]
            soln[i] = L[i] + R[i]
        # print(R)
        return soln

    def minOperations(self, boxes: str) -> List[int]:
        return Solution.DPMinOperations(boxes)

if __name__ == '__main__':
    solver = Solution()
    print(solver.minOperations("110"))
