import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for x in tokens:
            try:
                nums.append(int(x))
            except ValueError:
                if x == "+":
                    result = 0
                    for i in range(2):
                        result += nums[-1]
                        nums.pop()
                    nums.append(result)
                if x == "-":
                    result = nums[-2] - nums[-1]
                    for i in range(2):
                        nums.pop()
                        
                    nums.append(result)
                if x == "*":
                    result = nums[-2] * nums[-1]
                    for i in range(2):
                        nums.pop()
                    nums.append(result)

                if x == "/":
                    result = math.trunc(nums[-2] / nums[-1])
                    for i in range(2):
                        nums.pop()
                    nums.append(result)

        return nums[0]
