class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                k = i

        left, right = 0, k-1
        while left < right:
            mid = left + (right - left) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        l, r = k, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            return l
        return -1
        
