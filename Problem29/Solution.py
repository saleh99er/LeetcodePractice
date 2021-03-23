class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 # wtf leetcode

        sign = -1 if dividend < 0 or divisor < 0 else 1
        if dividend < 0 and divisor < 0:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        d_m = divisor
        factor = 1
        while(dividend > 0):
            if d_m + d_m <= dividend:
                d_m += d_m
                factor += factor
            else:
                d_m = divisor
                factor = 1
            dividend = dividend-d_m
            if dividend >= 0:
                result += factor
        if sign == -1:
            result = 0-result
        
        if result > 2147483647 or result < -2147483648:
            return 2147483647
        else:
            return result

if __name__ == '__main__':
    solver = Solution()
    print(solver.divide(-2147483648,-1))