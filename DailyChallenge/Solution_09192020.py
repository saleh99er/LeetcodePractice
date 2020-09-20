from collections import deque
from typing import List
"""
 Sequential Digits
 An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
 Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 input: low = 100, high = 300
 output: [123, 234]

 input: low = 1000, high = 13000
 output: [1234,2345,3456,4567,5678,6789,12345]

2000 -> 2345 check

2, 0 + (3-0), 0, 0

9000 -> upgrade digits needed, 10,000

"""

class Solution:
    """
      Definitely could use a code cleanup and some refactoring but the approach 
      is to start with the lowest number, incrementally adjust it to a sequential
      digit number by referencing the previous digit, adding one to that and 
      setting the current digit to this. If a digit ends up above 9 or is not 
      within the range, we need to readjust the current number under consideration
      by increasing the leftmost digit by one or increase the number of digits by
      one. 
    """
    def sequentialDigits_alt(self, low: int, high: int) -> List[int]:
        """
          Old soln
          Runtime: 32ms
          Memory usage: 14MB
          Better than 53.42% of python3 submissions for runtime
          Better than 16.84% of python3 submissions for memory
        """
        num = low
        soln = []
        bad_digit = False
        while(num < high):
          digits = math.floor(math.log10(num)) + 1

          # attempt to create a num soln from the previous answer
          for index in range(digits):
            if(index > 0):
              prev_index = index-1
              prev_digit = num // (10**(digits-prev_index-1)) % 10
              cur_digit = num // (10**(digits-index-1)) % 10
              # reassign num to  num = num + (prev_digit + 1 - cur_digit)*10**index
              new_digit = prev_digit + 1 - cur_digit
              if new_digit+cur_digit > 9:
                bad_digit = True
                break # can't make more solns with current digits, need to increase leftmost digit
              num = num + new_digit*(10**(digits-index-1))

          leftmost_digit = cur_digit = num // (10**(digits-1)) % 10
          # print(leftmost_digit+digits-1)
          if (num <= high and num >= low and not bad_digit):
            # print("new soln: %d" % num)
            soln.append(num)
            num = num + 10**(digits-1) # add to leftmost digit by 1
          elif((leftmost_digit+digits-1) < 11 and not bad_digit):
            # can attempt another soln w/ same number of digits
            num = num + 10**(digits-1) # add to leftmost digit by 1
            # print("attempting soln w/ same digits: %d" % num)
          else:
            num = 10**(digits)
            # print("trying again with 1 more digit")
          bad_digit = False
        # print(soln)
        return soln
    def sequentialDigits(self, low: int, high: int) -> List[int]:
      """
      Inspired by https://www.youtube.com/watch?v=mpwUf_JpCeI&ab_channel=NareshGupta
      Runtime: 24ms
      Memory usage: 13.7 MB
      Runtime beat 93.95% of submissions
      Memory usage beat 90.26% of submissions
      """
      solns = deque([])
      queue = deque([1, 2, 3, 4, 5, 6, 7, 8 ,9])
      while(len(queue) > 0):
        current_num = queue.popleft() 
        if(current_num >= low and current_num <= high):
          solns.append(current_num)
        last_digit = current_num % 10
        next = current_num*10 + last_digit + 1 # generate the next sequencial number that appends to this digit
        if(last_digit < 9 and next <= high):
          queue.append(next) # consider for making more possible solns
      return list(solns)
      
          

if __name__ == '__main__':
  soln = Solution()
  print(soln.sequentialDigits(58, 155))
  print(soln.sequentialDigits(200, 300))
  print(soln.sequentialDigits(1000, 13000))


          

