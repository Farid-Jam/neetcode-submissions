class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""
        def dfs(countOpen, countClose):
            nonlocal curr

            if len(curr) == n * 2:
                res.append(curr)
                return
            if countOpen < n:
                curr += '('
                dfs(countOpen + 1, countClose)
                curr = curr[:-1]
            if countClose < countOpen:
                curr += ')'
                dfs(countOpen, countClose + 1)
                curr = curr[:-1]
        dfs(0, 0)
        return res
            