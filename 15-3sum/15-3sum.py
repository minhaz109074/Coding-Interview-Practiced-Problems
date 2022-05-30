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
                    trip = sorted([nums[i], nums[l], nums[r]])
                    s.add(tuple(trip))
                    l += 1
                    r -= 1
                
        return s