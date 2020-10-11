"""
Problem 5: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Runtime: 1260 ms, faster than 57.57% 
Memory Usage: 14.1 MB, less than 8.06%
Runtime complexity: O(n^2)
Space complexity: O(n)

alt approach w/ DP (space and time of O(n^2)) ):
S_x := character of string s at index x
We define P(i,j) as following:

P(i,j) = true iff substring S_i .. S_j is a palindrome, false OW

Therefore,
P(i, j) = P(i+1, j-1) and S_i == S_j

The base cases are (for all i):
P(i, i) = true
P(i,i)=true

Once all have been evaluated find the longest distance indices
that evaluate to true in our memoization table. 

"""

class Solution:

    def longestPalindrome(self, s: str) -> str:
      s_length = len(s)
      longest = ''
      for index, char in enumerate(s):
        # odd char detection of palindrome "char in the center w/ left and 
        #     right substrings are identical"
        #print(index, char)
        left_index = index
        right_index = index
        local_palindrome = ''
        while(left_index >= 0 and right_index < s_length):
          if(s[left_index] != s[right_index]):
            break
          else:
            local_palindrome = s[left_index:right_index+1]
          left_index -= 1
          right_index += 1

        # even char detection of palindrome "mirror chars"
        left_mirror_index = index
        right_mirror_index = index+1
        while(right_mirror_index < s_length and left_mirror_index >= 0):
          if(s[left_mirror_index] != s[right_mirror_index]):
            break
          elif(right_mirror_index - left_mirror_index + 1 > len(local_palindrome)):
            local_palindrome = s[left_mirror_index:right_mirror_index+1]
          left_mirror_index -= 1
          right_mirror_index += 1

        if(len(longest) < len(local_palindrome)):
          longest = local_palindrome
          
      return longest

        

if __name__ == '__main__':
  solver = Solution()
  soln1 = solver.longestPalindrome("babad")
  soln2 = solver.longestPalindrome("cbbd")
  soln3 = solver.longestPalindrome('a')
  soln4 = solver.longestPalindrome('c')
  #print(soln2)
  print(soln1,soln2, soln3, soln4)