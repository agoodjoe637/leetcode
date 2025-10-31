from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        
        uniqueNums = set()
        
        for x in nums:
            if x in uniqueNums:
                result.append(x)
            else: 
                uniqueNums.add(x)
                
        return result
        