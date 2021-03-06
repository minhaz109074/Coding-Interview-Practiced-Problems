class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #TC: (log(maxP)*len(piles))
        left, right = 1 , max(piles)
        while(left < right):
            mid = (left + right)//2
            time = 0
            for val in piles:
                time += math.ceil(val/mid)
            if time <= h:
                right = mid
            else:
                left = mid + 1
        return right
            
        
        