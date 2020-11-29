from math import ceil

"""
  Problem 781: Rabbit in Forrest

  In a forest, each rabbit has some color. Some subset of rabbits (possibly all
  of them) tell you how many other rabbits have the same color as them. Those 
  answers are placed in an array. Return the minimum number of rabbits that 
  could be in the forest.
  
  Approach: use a dictionary to map reported population by a bunny (key) to the
  amount of bunnies that reported this population so far. This way we can keep
  track of which bunnies could belong to which group and the min number of 
  groups possible per population count. 
  
  Runtime complexity: O(n)
  Space complexity: O(n)
  Runtime: 40ms, faster than 74.09% of submissions
  Memory: 14.3 MB, less than 70.45% of submissions

"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        found = {}
        for reported_number in answers:
            if reported_number in found:
                found[reported_number] += 1
            else:
                found[reported_number] = 1
                
        rabbit_count = 0
        
        for reported_number in found:
            rabbit_per_group = reported_number+1
            if found[reported_number] >= rabbit_per_group: 
            	# 2 or more groups with same population report number
                num_groups = ceil(found[reported_number] / rabbit_per_group)
            else:
                num_groups = 1
            rabbit_count += num_groups*rabbit_per_group
        
        return rabbit_count
