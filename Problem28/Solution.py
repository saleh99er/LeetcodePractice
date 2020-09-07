"""
Problem 28: Implement strStr()
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def iterativeApproach(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        m := length of haystack
        n := length of needle

        runtime: O(m*n)
        space: O(1)
        runtime: 36ms, faster than 57.29%
        memory: 14.1 MB, less than 73.61%
        """
        needle_pos = 0
        haystack_pos = 0
        while(needle_pos < len(needle) and haystack_pos < len(haystack)):
            if(needle[needle_pos] == haystack[haystack_pos]):
                needle_pos += 1
                haystack_pos += 1
            else:
                haystack_pos -= (needle_pos-1)
                needle_pos = 0
                 
            
        
        if needle_pos == len(needle):
            return haystack_pos - needle_pos
        else:
            return -1

    def trivialApproach(haystack, needle):
        """
        runtime: avg -> O(n), worst -> O(n*m)
        Faster than 87.44%, 28ms; 14.1 MB, less than 32.5%
        applies Boyer-Moor string-search algo, utilizing pre-processing. 
        space: worst-case Pheta(k)

        'Boyer–Moore algorithm uses information gathered during the 
         preprocess step to skip sections of the text, resulting in a
         lower constant factor than many other string search algorithms.
         In general, the algorithm runs faster as the pattern length 
         increases. The key features of the algorithm are to match on 
         the tail of the pattern rather than the head, and to skip along
         the text in jumps of multiple characters rather than searching
         every single character in the text.'

        https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
        """
        return haystack.find(needle)

    def strStr(self, haystack, needle):
        return Solution.iterativeApproach(haystack, needle)

    
    

if __name__ == '__main__':
    solver = Solution()
    soln1 = solver.strStr("hello", "ll")
    soln2 = solver.strStr("aaaa", "bba")
    soln3 = solver.strStr("hey","")
    soln4 = solver.strStr("mississippi", "issip")
    print(soln1, soln2, soln3, soln4)
        