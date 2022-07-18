class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curComb, curSum, index):
            if curSum > target:
                return
            if curSum == target:
                ans.append(curComb[:])
                return
            for i in range(index, len(candidates)):
                curComb.append(candidates[i])
                curSum += candidates[i]
                backtrack(curComb, curSum, i)
                curComb.pop()
                curSum -= candidates[i]
        
        backtrack([],0,0)
        return ans
        