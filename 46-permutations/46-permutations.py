class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i,val in enumerate(nums):
                if used[i]:
                    continue
                path.append(val)
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False
                
        backtrack([], [False]*len(nums))
        return ans
        