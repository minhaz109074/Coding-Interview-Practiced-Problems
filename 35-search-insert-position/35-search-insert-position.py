class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def condition(value) -> bool:
            return nums[value] >= target

        left, right = 0, len(nums)-1
        if nums[right]< target: return right+1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left