

"""
Problem 1689: Partioning into min number of Deci-Binary Numbers

a decimal number is called deci-binary if each of its digits is either 0 or 1 
without any leading zeros. For example, 101 and 1100 are deci-binary, while
112 and 3001 are not. Given a string n that represents a positive decimal 
integer, return the minimum number of positive deci-binary numbers needed so 
that they sum up to n.

Solution: An intuition that helps is given the largest value number in all the 
digits is x, you need x deci-binary numbers to have their sum add up to n. So
a linear search that finds the largest value digit and outputs that (which is
at most 9) is all that's needed.

Assumption: minPartitions of n = "0" is 0 and minPartitions of n = "" is 0.

N := chars in string n
Runtime Complexity : O(N)
Space Complexity: O(1)
Runtime: 292ms, faster than 15.84%
Memory: 14.8 MB, less than 35.72%

"""

class Solution:
    def minPartitions(self, n: str) -> int:
        largest_digit = 0
        for digit_str in n:
            largest_digit = max(largest_digit,int(digit_str))
            if largest_digit == 9:
                return largest_digit
        return largest_digit

if __name__ == "__main__":
    solver = Solution()
    assert 3 == solver.minPartitions("32")
    assert 8 == solver.minPartitions("82734")
    assert 9 == solver.minPartitions("27346209830709182346")