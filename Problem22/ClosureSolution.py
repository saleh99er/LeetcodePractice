"""
Leetcode solution using closure number on Problem 22 copied directly

Intuition: For each closure number c, we know the starting and ending brackets
 must be at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid
 sequence, plus the rest of the elements must be a valid sequence.

 Runtime: O(4^n / sqrt(n))
 Space: O(4^n / sqrt(n))
"""

class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans