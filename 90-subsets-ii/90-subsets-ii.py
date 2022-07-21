class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end, subset):
            ans.append(subset[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1, end, subset)
                subset.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans
        