class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        ans = []
        h = []
        for key,val in m.items(): # loop takes O(n) time  # push takes O(logn) time # so TC: O(nlogn)
            heappush(h,(-val, key))  # by default python heap is minheap. by multiplying -1 to the val we                                        #make this heap a max heap
                                   
        count = 0
        while count<k:
            ans.append(heappop(h)[1]) # O(klogk) #we take only item not frequency
            count += 1
            
        return ans
                
                     
                
        
            
        
        
        
        