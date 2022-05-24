class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(n), SC: O(n)
        
                                                 # [0,1,2,.....]
        freq = [[] for _ in range(len(nums)+1)]  # [[][][].....]
        ans = []
        for key, val in Counter(nums).items():
            freq[val].append(key)          # for [1,1,1,2,2,3] -> [[][3][2][1][][][]] 
        for i in reversed(range(len(nums)+1)):
            for num in freq[i]:
                ans.append(num)             #this loop takes avg case O(1) time
                if len(ans) == k: return ans  # in worst case when all valuse are unique it takes O(n) time for only one i
                                              # so technically for 2for loops it takes O(n) time
                    
                                  
                                
        
                
                     
                
        
            
        
        
        
        