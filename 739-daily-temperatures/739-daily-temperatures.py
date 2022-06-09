class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        stack.append((temperatures[0], 0))
        for i in range(1, n):
            while stack and stack[-1][0]<temperatures[i]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))
            
        return ans

                    
            
        
        