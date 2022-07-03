class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums)-1
        minval = nums[right]
        while left <= right :
            mid = (left + right) >> 1
            minval = min(minval, nums[mid])
            
            if nums[left] <= nums[mid]:
                minval = min(minval,nums[left])
                left = mid + 1
            else:
                right = mid - 1
                
        return minval
                
        