from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def findLeft( nums, target):
            index = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    index = mid

            return index

        def findRight( nums, target):
            index = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1

                if nums[mid] == target:
                    index = mid
            return index
        left_index = findLeft(nums,target)
        right_index = findRight(nums,target)
        return [left_index,right_index]
    
