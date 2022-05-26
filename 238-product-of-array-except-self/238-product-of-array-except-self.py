class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = nums.count(0)
        for i in range(len(nums)):
            if nums[i]: prod *= nums[i]    
        if zerocount > 1: return [0]*len(nums)          
        for i in range(len(nums)):
            if zerocount: nums[i] = 0 if nums[i] else prod   
            else: nums[i] = prod // nums[i]     
        return nums