class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = 0,0
        numclone = sorted(nums)
        flag = False
        for i in range(len(nums)):
            if flag == False and nums[i] != numclone[i]:
                flag = True
                l = i
            if flag == True and nums[i] != numclone[i]:
                r = i
                
        return r-l+1 if r else 0
                
            