""" 
    Problem 39, Combination Sum
    Had to check the hints and took a while to realize how to avoid permutations of prev discovered solns
    
    
    Runtime complexity: O(N^2)
    Runtime: 72ms, faster than 72.77% of submissions
    Space complexity: O(N^2)
    Space: 13.8 MB, less than 71.02% of submissions
"""
from typing import List


class Solution:
    solns = []
    
    def combFinder(accum, index, candidates, target):
        for index in range(index, len(candidates)):
            candidate = candidates[index]
            accum.append(candidate)
            if(candidate == target):
                Solution.solns.append(accum.copy()) # Add accumulated sum to soln
            else:
                leftover = target - candidate
                if(leftover > 0):
                    Solution.combFinder(accum, index, candidates, leftover)
            accum.remove(candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        Solution.solns.clear()
        Solution.combFinder( [], 0, candidates, target)
        return Solution.solns
        
if __name__ == '__main__':
    x = Solution()
    soln = x.combinationSum([2,3,6,7], 7)
    print(soln)