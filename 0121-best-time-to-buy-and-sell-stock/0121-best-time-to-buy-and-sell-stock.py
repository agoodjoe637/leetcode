from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        current_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = max(current_profit, prices[right] - prices[left])
                
            else:
                left = right
                
            right += 1

        return current_profit