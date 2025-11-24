from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        def insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j][1] < key[1]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        freq_list = list(freq.items())

        insertion_sort(freq_list)

        return [item[0] for item in freq_list[:k]]
