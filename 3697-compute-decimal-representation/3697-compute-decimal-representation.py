from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        answer = []
        k = 1
        while n > 0:
            mod = n % pow(10, k)
            if mod != 0:
                answer.insert(0, mod)
                n = n - mod
            k += 1
        return answer
