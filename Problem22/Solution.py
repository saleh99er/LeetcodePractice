"""
  Problem 22: Generate Parentheses

  Given n pairs of parentheses, write a function to generate all combinations 
  of well-formed parentheses.
  
  for example, given n = 3, a solution set is 
  ['((()))', '()(())', '(())()', '(()())', '()()()']

"""

from typing import List, Deque
from collections import deque

class Solution:
    def removeDuplicates(input_list: List) -> List:
      return list(dict.fromkeys(input_list))

    def parenStrList(n: int, accum: Deque[str]) -> Deque[str]:
      if n == 0:
        return accum

      accum_length = len(accum)
      if accum_length == 0:
        accum.append('()')
      else:
        for i in range(accum_length):
          n_minus_1_paren_str = accum.popleft()
          accum.append('(' + n_minus_1_paren_str + ')')
          accum.append('()' + n_minus_1_paren_str)
          accum.append(n_minus_1_paren_str + '()')
          nested = 0
          for index, char in enumerate(n_minus_1_paren_str):
            if char == '(':
              nested += 1
            elif char == ')':
              nested -= 1
            if nested == 0 and index < len(n_minus_1_paren_str) - 1:
              substring_paren = n_minus_1_paren_str[:index+1]
              remaining_paren = n_minus_1_paren_str[index+1:]
              # print(n_minus_1_paren_str, ":", substring_paren, ":", remaining_paren)
              accum.append('(' + substring_paren + ')' + remaining_paren)
              accum.append(substring_paren + '(' + remaining_paren + ')')
      return Solution.parenStrList(n-1, accum)

    def generateParenthesis(self, n: int) -> List[str]:
      solns_with_duplicates = list(Solution.parenStrList(n, deque()))
      return Solution.removeDuplicates(solns_with_duplicates) 

if __name__ == '__main__':
  solver = Solution()
  print(solver.generateParenthesis(3))
        