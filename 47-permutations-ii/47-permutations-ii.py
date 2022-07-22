class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False
                
        backtrack([], [False]*len(nums))
        return ans