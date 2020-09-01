import random
"""
Problem 169: Majority Element
"""

class Solution(object):

    def firstAttempt(self, nums):
        """O(n) memory and O(n) runtime complexity"""
        voteDict = {}
        for num in nums: # O(n)
            if num in voteDict: # O(1)
                voteDict[num] += 1
            else:
                voteDict[num] = 1
        
        majority = None
        for num in voteDict: # O(n)
            if majority is None or voteDict[majority] < voteDict[num]: # O(1)
                majority = num
        return majority

    def secondAttempt(self, nums):
        """O(1) memory and O(infinity [worstcase], 1 [avg case]) runtime complexity"""
        foundMajority = False
        while(not foundMajority):
            randomEl = random.choice(nums)
            occurence = 0
            for num in nums:
                if(num == randomEl):
                    occurence += 1
            if(occurence > len(nums)/2):
                foundMajority = True
        return randomEl
    
    def majorityElement(self, nums):
        return self.secondAttempt(nums)

        


if __name__ == '__main__':
    x = Solution()
    print("Answer: %d" % x.majorityElement([3,3,4]))