class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(curComb, curSum, index):
            if curSum == target:
                ans.append(curComb[:])
            elif curSum < target:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    curComb.append(candidates[i])
                    curSum += candidates[i]
                    backtrack(curComb, curSum, i+1)
                    curComb.pop()
                    curSum -= candidates[i]
            return
        
        backtrack([], 0, 0)
        return ans