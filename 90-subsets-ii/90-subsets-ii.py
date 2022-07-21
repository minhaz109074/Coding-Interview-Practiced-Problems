class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end, subset):
            ans.add(tuple(subset[:]))
            for i in range(start, end):
                subset.append(nums[i])
                backtrack(i+1, end, subset)
                subset.pop()
        ans = set()
        nums.sort()
        backtrack(0, len(nums), [])
        return ans
        