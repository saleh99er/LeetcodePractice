"""
  Problem 7: Reverse Integer

  Given a 32-bit signed integer, reverse digits of an integer. Assume we are 
  dealing with an environment that could only store integers within the 32-bit
  signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
  assume that your function returns 0 when the reversed integer overflows.

  321 -> 123


"""

class Solution:
    def reverse(self, x: int) -> int:
      """
      Iterative approach
      n := number of digits of x, ceil(log10(x))
      Time: O(n) (assuming constant time operations)
      Space: O(1)
      Runtime: 32ms, faster than 67.74% of submissions
      Memory: 14.1 MB, less than 7.88% of submissions
      """
      multiplier = 1
      accum = 0

      if x < 0:
        multiplier = -1
        x = -x
      
      remaining_digits = x
      while(remaining_digits > 0):
        least_sig_digit = remaining_digits % 10
        accum = accum*10 + least_sig_digit
        remaining_digits = remaining_digits // 10 
      
      soln = multiplier*accum

      if soln > 2**31 - 1 or soln < -2**31: 
        return 0
      else: 
        return soln
    
    def reverse_digits(accum: int, remaining_digits: int, multiplier: int) -> int:
      """
      Recursive approach helper function
      """
      if accum > 2**31 - 1 or accum < -2**31:
        return 0
      elif remaining_digits == 0:
        return multiplier * accum
      else:
        least_sig_digit = remaining_digits % 10
        accum = accum*10 + least_sig_digit
        remaining_digits = remaining_digits // 10
        return Solution.reverse_digits(accum, remaining_digits, multiplier)

    def reverse_digits_recursive(self, x: int) -> int:
      """
      Recursive approach
      n := number of digits of x, ceil(log10(x))
      Time: O(n) (assuming constant time operations)
      Space: O(n) (tail recursion optimization isn't present in python)
      Runtime: 32ms, faster than 67.74% of submissions
      Memory: 14.3 MB, less than 5.22% of submissions
      """
      if x < 0:
        return Solution.reverse_digits(0, -1*x, -1)
      else:
        return Solution.reverse_digits(0, x, 1)




if __name__ == '__main__':
  solver = Solution()
  print(solver.reverse(321))
  print(solver.reverse(-1 * 2**31))
  print(solver.reverse(-123))
  print(solver.reverse(1534236469))