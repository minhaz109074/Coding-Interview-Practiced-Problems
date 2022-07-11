class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [('(', 1, 0)]
        while stack:
            x, l, r = stack.pop()
            if len(x) == 2*n:
                ans.append(x)
                continue
            if l<n:
                stack.append((x+'(', l+1, r))
            if r<l:
                stack.append((x+')', l, r+1))
        return ans
                
            
        
        
        
        
        