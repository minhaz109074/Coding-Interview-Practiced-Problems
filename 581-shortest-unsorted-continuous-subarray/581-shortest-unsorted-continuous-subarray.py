class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        Max,Min = nums[0], nums[n-1]
        beg, end = -1, -2  # for sorted array end - beg + 1 -> -2-(-1)+1 = 0
        for i in range(n):
            Max = max(Max, nums[i])
            Min = min(Min, nums[n-1-i])
            if Max>nums[i]:
                end = i
            if Min<nums[n-1-i]:
                beg = n-1-i
              
        return end - beg + 1
                
            