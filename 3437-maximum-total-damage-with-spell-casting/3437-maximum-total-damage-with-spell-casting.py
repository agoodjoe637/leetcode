from typing import List
from collections import defaultdict


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        nums = defaultdict(int)

        for x in power:
            nums[x] += x

        unique_nums = list(set(power))
        unique_nums.sort()

        memory = {}

        def sum_max(index):
            if index >= len(unique_nums):
                return 0

            if index in memory:
                return memory[index]

            nextValid = index + 1

            while nextValid < len(unique_nums) and unique_nums[nextValid] in range(
                unique_nums[index], unique_nums[index] + 3
            ):
                nextValid += 1

            result = max(
                nums[unique_nums[index]] + sum_max(nextValid), sum_max(index + 1)
            )

            memory[index] = result

            return result

        return sum_max(0)
