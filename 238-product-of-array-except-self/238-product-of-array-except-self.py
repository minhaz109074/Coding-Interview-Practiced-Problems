class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        left, right = 1, 1
        # instead of using two separate loop for left and right value calculation, we just did it
        # in one single pass by using another pointer n-1-i from reverse for right values
        for i in range(n):
            ans[i] *= left
            left = left*nums[i]
            ans[n-1-i] *= right     
            right = right*nums[n-1-i]

        return ans