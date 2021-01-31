from collections import Counter

"""
Problem 76: Minimum Window Substring (Hard)

Given two strings s and t, return the minimum window in s which will contain
all the characters in t. If there is no such window in s that covers all 
characters in t, return the empty string "".

Assumption: Duplicate characters in t (x occurences) need just as many 
duplicates in s.

Approach: First confirm enough letter occurrences in s are present to contain
the letters of t. If so then a valid window exists in s (OW return empty 
string). We will have a dictionary/counter that will count the occurences
of each letter for t and u (our window of s) respectfully. Then we will rely
on 2 pointers looping from left to right both initially on the first element 
in s. We will check if a window is valid by seeing if each unique char in t 
is satisfied with the letter occurence for each corresponding letter. This 
allows us to only compare a single dictionary pair from s and t per window
change. If we have a valid window, attempt to shrink it by moving the left
pointer forward by one. If we don't have a valid window, expand it by moving 
the right pointer forward by one. If a valid window is smaller length than
the best solution known so far, overwrite it. Return the found solution once
the right pointer is at the end and the left pointer is no longer shrinking.


(looked at soln to get this one)

N := length of S + length of T

Runtime complexity: O(N)
Memory complexity: O(N)
Runtime: 248 ms, faster than 20.28% of submissions
Memory: 14.9 MB, less than 70.03% of submissions
"""

class Solution:

    def checkIfCharSat(new_char: str, s_counter, t_counter, old_chars_sat_count: int):
        if t_counter[new_char] == s_counter[new_char]:
            return old_chars_sat_count + 1
            
        else:
            return old_chars_sat_count
            
    def checkIfCharUnsat(removed_char: str, s_counter, t_counter, old_chars_sat_count: int):
        if t_counter[removed_char] <= s_counter[removed_char]:
            return old_chars_sat_count
        else:
            return old_chars_sat_count - 1

    def minWindow(self, s: str, t: str) -> str:
        t_char_freq = Counter(t)
        s_whole_freq = Counter(s)
        
        if len(t_char_freq-s_whole_freq) > 0 or len(s) < 1 or len(t) < 1:
            return "" # s does not have all of t chars
        
        s_char_freq = Counter(s[0])
        s_count = 1
        unique_t_chars = len(t_char_freq)
        unique_chars_satisfied = Solution.checkIfCharSat(s[0], s_char_freq, t_char_freq, 0)
        l = 0
        r = 0
        last_r_added = s[0]
        is_valid_window = False
        best_window = s
        while(r<len(s)):
            #print("r iteration")
            # Check if current window is valid
            if s_count >= len(t) and unique_chars_satisfied == unique_t_chars:
                is_valid_window = True
                #print("found valid window: l = %d, r = %d" % (l,r))
                if len(best_window) > r+1-l:
                    best_window = s[l:r+1]
                
                # Shrink window from the left until invalid
                while(l < r and is_valid_window):
                    l += 1
                    old_l_el = s[l-1]
                    s_char_freq[old_l_el] -= 1
                    s_count -= 1
                    
                    unique_chars_satisfied = Solution.checkIfCharUnsat(old_l_el, s_char_freq, t_char_freq, unique_chars_satisfied)
                    
                    if s_count >= len(t) and unique_chars_satisfied == unique_t_chars:
                        #print("optimizing window: l = %d, r = %d" % (l,r))
                        is_valid_window = True
                        if len(best_window) > r+1-l:
                            best_window = s[l:r+1]
                    else:
                        is_valid_window = False
                        
            # Find a valid window, expanding rightward
            r += 1
            if r < len(s):
                last_r_added = s[r]
                s_char_freq[last_r_added] += 1
                s_count += 1
                unique_chars_satisfied = Solution.checkIfCharSat(last_r_added, s_char_freq, t_char_freq, unique_chars_satisfied)
                    
        return best_window
        
if __name__ == '__main__':
    solver = Solution()
    #print(solver.minWindow("ABAACBAB", "ABC"))
    #print(solver.minWindow("A", "A"))
    #print(solver.minWindow("ADOBECODEBANC", "ABC"))
    print(solver.minWindow("cabwefgewcwaefgcf", "cae"))
