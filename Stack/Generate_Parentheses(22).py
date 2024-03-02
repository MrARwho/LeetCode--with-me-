class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def goback(l: int, r: int, s: str) -> None:
            if l == 0 and r == 0:
                ans.append(s)
            if l > 0:
                goback(l - 1, r, s + '(')
            if l < r:
                goback(l, r - 1, s + ')')

        goback(n, n, '')
        return ans