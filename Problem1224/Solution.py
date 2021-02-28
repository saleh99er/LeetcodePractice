from typing import List

"""
Problem 1224: Maximum Equal Frequency (Hard)

Given an array nums of positive integers, return the longest possible length of
an array prefix of nums, such that it is possible to remove exactly one element
from this prefix so that every number that has appeared in it will have the
same number of occurrences. If after removing one element there are no
remaining elements, it's still considered that every appeared number has the
same number of ocurrences (0).

Assumption: prefix means a subarray where the beginning pointer is at index 0
and the end pointer < len(array)

Intuition: Only a 1 dimensional scan of where the end pointer should be is
needed. (until I looked at a solution I didn't know this constraint was
present) Also any solution is of at least length two because removing either
two elements will give an equal frequency of 1 for the remaining element.

Approach: Linear search with two dictionaries (freq to unique element values
and element value to frequency). At index i update dictionary to include this
elements. If there is only one freq among elements 0 to i  and that freq is 1
or there is only 1 unique element then this is a valid prefix. An alternative
case is if there are two frequencies and the greater frequency is only one
above the other or one of the two frequencies is 1. This is also a valid
prefix. If a valid prefix, update the longest prefix length found so far to
i+1.

Runtime complexity: O(n)
Space complexity: O(n)
Runtime: 616ms, faster than 62.28%
Space: 21.6 MB, less than 85.96%

(Saw ojha1111pk's solution, thanks for sharing this in the Discuss tab)
"""


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq_to_el = {}
        el_to_freq = {}
        if len(nums) == 0:
            return nums

        # Initial global solution, first element in nums (2 if len(nums) > 1)
        freq_to_el[1] = 1
        el_to_freq[nums[0]] = 1
        longest_eq_freq_prefix_len = 1

        for end_pointer in range(1,len(nums)):
            # Add el to dictionaries
            el = nums[end_pointer]
            if el in el_to_freq:
                old_freq = el_to_freq[el]
                el_to_freq[el] += 1
                freq_to_el[old_freq] -= 1
                if freq_to_el[old_freq] == 0:
                    del freq_to_el[old_freq]
                new_freq = old_freq+1
                if new_freq not in freq_to_el :
                    freq_to_el[new_freq] = 1
                else:
                    freq_to_el[new_freq] += 1
            else:
                el_to_freq[el] = 1
                if 1 in freq_to_el:
                    freq_to_el[1] += 1
                else:
                    freq_to_el[1] = 1

            # Determine if equal freq can occur with one element removed
            valid_prefix = False
            #print(end_pointer, freq_to_el)
            if (len(freq_to_el) == 1 and
                (1 in freq_to_el or len(el_to_freq) == 1)):
                 valid_prefix = True  # all_el_freq_of_one
                 #print("1st case, ", end_pointer)
            elif (len(freq_to_el) == 2):
                freqs = list(freq_to_el.keys())
                first_freq = freqs[0]
                second_freq = freqs[1]
                one_el_one_freq = ((freq_to_el[first_freq] == 1 and
                                    first_freq == 1) or
                                   ((freq_to_el[second_freq] == 1 and
                                     second_freq == 1)))
                one_el_up_freq = (abs(first_freq - second_freq) == 1 and
                                  freq_to_el[max(first_freq,second_freq)] == 1)
                if (one_el_one_freq or one_el_up_freq):
                    valid_prefix = True
                    #print("2nd case, ", end_pointer)
            if valid_prefix:
                longest_eq_freq_prefix_len = end_pointer+1

        return longest_eq_freq_prefix_len

if __name__ == '__main__':
    input_arr = [1,1,1,2,2,2,3,3,3,4,4,4,5]
    solver = Solution()
    print(solver.maxEqualFreq(input_arr))
