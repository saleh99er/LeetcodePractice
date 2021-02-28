from typing import List

"""
Problem 121: Best Time to Buy and Sell Stock (Easy)

You are given an array prices where prices[i] is the price of a given stock on
the ith day. You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that stock. Return
the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Approach: We can build a solution using two intuitions. Let S be the index/day
we sell a stock and B be the index/day we buy a stock, therefore B < S. First,
if Price[S] - Price[B] < 0 (LHS of inequality is profit) we know any
indices/days after S could reap better profits if we bought the stock at S
instead of B, so before considering all other stocks after S, we should
readjust the B index to S's location and consider selling sometime after B.
Second, if we have positive profit with our current B and S, we can buy at B
price and sell at a higher profit if we can find an S' s.t. S' > S and
Price[S'] > Price[S]. Combining these two strategies we have a two pointer
window algorithm that can find the buy and sell indices that maximize profits.

N := len(prices)
Runtime complexity: O(n)
Space complexity: O(1)
Runtime: 1032 ms, faster than 17.38%
Memory: 25.2 MB, less than 12.66%

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        len_prices = len(prices)
        if len_prices < 2:
            return 0
        else:
            buy_index = 0
            sell_index = 1
            while sell_index < len_prices:
                if prices[sell_index] < prices[buy_index]:
                    buy_index = sell_index
                    sell_index += 1
                else:
                    local_profit = prices[sell_index]-prices[buy_index]
                    best_profit = best_profit if best_profit > local_profit else local_profit
                    sell_index += 1
            return best_profit
