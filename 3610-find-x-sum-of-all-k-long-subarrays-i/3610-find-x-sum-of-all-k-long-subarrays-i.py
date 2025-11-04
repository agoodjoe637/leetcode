import sys
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums) - k + 1):
            frequencies = {}
            currentWindowSum = 0
            for j in range(k):
                current_element = nums[i + j]
                frequencies[current_element] = frequencies.get(current_element, 0) + 1

            if len(frequencies) < x:
                for value, frequency in frequencies.items():
                    currentWindowSum += value * frequency
            else:
                top_nums = []

                for _ in range(x):
                    top_value = max(frequencies, key=lambda k: (frequencies[k], k))
                    top_nums.append(top_value * frequencies[top_value])
                    del frequencies[top_value]

                currentWindowSum = sum(top_nums)
            answer.append(currentWindowSum)
        return answer
