from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivotIndex = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivotIndex = i
                break
        if pivotIndex == -1:
            nums.reverse()
            return

        for j in range(len(nums) - 1, pivotIndex, -1):
            if nums[j] > nums[pivotIndex]:
                nums[j], nums[pivotIndex] = nums[pivotIndex], nums[j]
                break
        left, right = pivotIndex +1, len(nums)-1
        
        while left < right:
            nums[left], nums[right]= nums[right], nums[left]
            left += 1
            right -= 1        