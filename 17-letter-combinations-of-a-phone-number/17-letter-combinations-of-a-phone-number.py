class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 0: return ans
        def backtrack(index, comb):
            if index == len(digits):
                ans.append(comb)
                return
            s = dic[digits[index]]
            for i in range(len(s)):
                comb += s[i]
                backtrack(index+1,comb)
                comb = comb[:-1]

        backtrack(0, "")
        return ans
        