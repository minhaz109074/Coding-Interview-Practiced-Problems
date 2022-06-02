class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        beg , end = 0, n-1
        maxwater = 0
        while(beg<end):
            curwater = (end-beg)*min(height[end], height[beg])
            if height[end] > height[beg]:
                beg += 1
            else:
                end -= 1
            maxwater = max(maxwater, curwater)
        return maxwater
            
            
       