from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = 0
        nums_set = set(nums)

        for x in nums_set:

            if x - 1 not in nums_set:
                length = 0
                while x + length in nums_set:
                    length += 1
                consec = max(consec, length)

        return consec
