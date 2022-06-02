class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        nums.sort()
        for i in range(n-2):
            l = i+1
            r = n-1
            while(l<r):
                cursum = nums[i] + nums[l] + nums[r]
                if cursum > 0:
                    r -= 1
                elif cursum < 0:
                    l += 1
                else:
                    s.add((nums[i], nums[l], nums[r]))
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                
        return s