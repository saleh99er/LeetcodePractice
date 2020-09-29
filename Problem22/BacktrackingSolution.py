"""
 Leetcode solution for backtracking force on Problem 22 copied directly
 
 crude approx for analysis but you can see a soln at each level splitting 
 between 2 binary choices, whether or not to put a left and a right parentheses
 at that index of the string respectively but this is not the tightest bound 
 since some of these are invalid (such as a close parenthesis without a matching
 open parentheis)

 Runtime: O(4^n / sqrt(n))
 Space: O(4^n / sqrt(n))
 Runtime: 28 ms, faster than 93.50% of submissions
 Memory Usage: 14.4 MB, less than 5.65% of submissions 

"""

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans