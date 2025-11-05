from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        top = SortedList()
        remainers = SortedList()
        frequencies = defaultdict(int)

        current_sum = 0

        def balance():
            nonlocal current_sum

            if len(top) > x:
                f, val = top.pop(0)
                remainers.add((f, val))
                current_sum -= f * val

            if len(top) < x and remainers:
                f, val = remainers.pop()
                top.add((f, val))
                current_sum += f * val

            if top and remainers and top[0] < remainers[-1]:
                f1, val1 = top.pop(0)
                f2, val2 = remainers.pop()
                top.add((f2, val2))
                remainers.add((f1, val1))
                current_sum += f2 * val2 - f1 * val1

        def add(num):
            nonlocal current_sum

            if num in frequencies:
                prev = (frequencies[num], num)
                if prev in top:
                    top.remove(prev)
                    current_sum -= frequencies[num] * num
                else:
                    remainers.remove(prev)

            frequencies[num] += 1
            top.add((frequencies[num], num))
            current_sum += frequencies[num] * num
            balance()

        def remove(num):
            nonlocal current_sum

            if num in frequencies:
                prev = (frequencies[num], num)
                if prev in top:
                    top.remove(prev)
                    current_sum -= frequencies[num] * num
                else:
                    remainers.remove(prev)

            frequencies[num] -= 1
            if frequencies[num] == 0:
                del frequencies[num]
            else:
                top.add((frequencies[num], num))
                current_sum += frequencies[num] * num

            balance()

        answer = []
        for i in range(k):
            add(nums[i])

        answer.append(current_sum)

        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            answer.append(current_sum)

        return answer
