class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_s1 = {}
        letters_s2 = {}

        window = len(s1)
        if len(s1) > len(s2):
            return False

        for i in s1:
            letters_s1[i] = 1 + letters_s1.get(i, 0)

        for i in range(window):
            letters_s2[s2[i]] = 1 + letters_s2.get(s2[i], 0)

        if letters_s1 == letters_s2:
            return True

        for i in range(len(s2) - window):
            letters_s2[s2[i]] -= 1
            if letters_s2[s2[i]] == 0:
                del letters_s2[s2[i]]
            letters_s2[s2[i + window]] = 1 + letters_s2.get(s2[i + window], 0)

            if letters_s1 == letters_s2:
                return True

        return False
