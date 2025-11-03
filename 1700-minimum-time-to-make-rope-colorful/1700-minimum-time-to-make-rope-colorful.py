from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        for x in range(len(colors) - 1):
            if colors[x] == colors[x + 1]:
                if neededTime[x] < neededTime[x + 1]:
                    time += neededTime[x]
                else:
                    time += neededTime[x + 1]
                    neededTime[x + 1] = neededTime[x]

        return time
