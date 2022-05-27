class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        left, right = 1, 1
        for i in range(len(nums)):
            ans.append(left)
            left = left*nums[i]
        for j in reversed(range(len(nums))):
            ans[j] *= right
            right = right*nums[j]
        
        return ans