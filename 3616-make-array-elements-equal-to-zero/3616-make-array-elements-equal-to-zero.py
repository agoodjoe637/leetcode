from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        zeroes = []
        valid = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)

        for j in zeroes:
            rightSum = 0
            leftSum = 0
            start = 0
            currentLeft = j
            currentRight = j
            end = len(nums) - 1

            while currentLeft > start:
                leftSum += nums[currentLeft - 1]
                currentLeft -= 1

            while currentRight < end:
                rightSum += nums[currentRight + 1]
                currentRight += 1

            if rightSum == leftSum:
                valid += 2
            elif abs(rightSum - leftSum) == 1:
                valid += 1

        return valid
