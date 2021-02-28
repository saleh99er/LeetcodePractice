from typing import List

"""
Problem 15: 3 Sum

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of 
zero.

Assuming I shouldn't revise nums

Approach: First have a sorted copy of nums then traverse in a linear fashion 
the first element for the sum (outer loop). Our inner loop will use pointers 
at one to the right of the first element and last element for the second and
third element respectively continuing this loop until the second and third 
pointer point to the same index. If the sum is < 0 or second prev element equals
second current element, move the second right; sum > 0 or third prev element 
equals third current element move third pointer left. OW the sum is equal to 0
append all three elements as a tuple in our solution list.  

Runtime: 2032 ms, faster than 18.78%
Memory Usage: 17.6 MB, less than 46.45%
Runtime Complexity: O(n^2)
Space Complexity: O(n)

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln = []
        sortedNums = nums.copy()
        sortedNums.sort()
        #print(sortedNums)
        for s,d_s in enumerate(sortedNums):
            # print(s, d_s)
            if s > 0 and sortedNums[s-1] == d_s:
                #print("skipping, dup d_s")
                continue 
            i = s+1
            j = len(nums)-1
            while(i < j and i < len(nums)):
                el_sum = d_s + sortedNums[i] + sortedNums[j]
                #print(d_s, sortedNums[i], sortedNums[j], el_sum)
                is_prev_i_same = i > s+1 and sortedNums[i] == sortedNums[i-1]
                is_prev_j_same = j < len(nums)-1 and sortedNums[j] == sortedNums[j+1]
                if el_sum == 0 and not is_prev_i_same and not is_prev_j_same:
                    soln.append([d_s, sortedNums[i], sortedNums[j]])
                    i += 1
                elif el_sum < 0 or is_prev_i_same:
                    i += 1
                elif el_sum > 0 or is_prev_j_same:
                    j -= 1
                else:
                    print("last case should never occur")
        return soln 

    
if __name__ == '__main__':
    solver = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solver.threeSum(nums))

