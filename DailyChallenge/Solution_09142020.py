class Solution:
    
    def access(nums, index):
        if(index < 0):
            return 0
        else:
            return nums[index]

    def rob(self, nums) -> int:
        """ 
        Dynamic Programming
        Space complexity: O(N)
        Time complexity: O(N)
        """
        if(len(nums) == 0):
            return 0
        
        N = len(nums)
        opt = [0]*N # Memoize opt soln from 0 to i

        # degenerative cases, opt[0] and opt[1]
        for i in range(N):
            select_i_max = Solution.access(nums,i) + Solution.access(opt, i-2)
            dont_select_i_max = Solution.access(nums,i-1) + Solution.access(opt, i-3)
            opt[i] = max(select_i_max, dont_select_i_max)
        return opt[N-1]

    def rob_strawman(self, nums) -> int:
        """
        Take advantage of problem specs, Greedy algo
        Try odds only and evens only and return max
        Space Complexity: O(1)
        Time Complexity: O(N)
        Counterexample: [2, 1, 1, 2]
        """
        N = len(nums)
        evens = range(0, N, 2)
        odds = range(1, N, 2)
        evens_sum = 0
        odds_sum = 0
        for index in evens:
            evens_sum += nums[index]
        for index in odds:
            odds_sum += nums[index]
        return max(odds_sum, evens_sum)


if __name__ == '__main__':
    x = Solution()
    print(x.rob([1,5,9,30]))