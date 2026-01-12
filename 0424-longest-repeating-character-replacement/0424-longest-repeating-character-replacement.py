class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        letters_dict = {}
        result = 0

        while right < len(s):
            letters_dict[s[right]] = 1 + letters_dict.get(s[right], 0)
            while (right - left + 1) - max(letters_dict.values()) > k:
                letters_dict[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result
