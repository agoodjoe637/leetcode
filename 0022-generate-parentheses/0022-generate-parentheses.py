class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parantheses = []
        answer = []

        def backTracking(open, close):
            if len(parantheses) == 2 * n:
                answer.append("".join(parantheses))
                return

            if open < n:
                parantheses.append("(")
                backTracking(open + 1, close)
                parantheses.pop()

            if open > close:
                parantheses.append(")")
                backTracking(open, close + 1)
                parantheses.pop()

        backTracking(0, 0)
        return answer
