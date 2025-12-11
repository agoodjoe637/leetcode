import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = math.inf

        def eat(k, piles):
            hours_to_eat = 0
            for x in piles:
                hours_to_eat += math.ceil(x / k)

            return hours_to_eat

        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            if eat(mid, piles) <= h:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1

        return result
