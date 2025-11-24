from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        elif len(strs) == 1:
            return [strs]

        words = defaultdict(list)

        for string in strs:
            sorted_word = "".join(sorted(string))
            words[sorted_word].append(string)

        return list(words.values())
