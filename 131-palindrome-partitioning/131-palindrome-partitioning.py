class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalindrome(string):
            n = len(string)
            for i in range(n//2):
                if string[i] != string[n-1-i]:
                    return False
            return True
        def backtrack(index, p):
            if  index == len(s):
                ans.append(p[:])
                return
            for i in range(index, len(s)):
                cur = s[index:i+1]
                if isPalindrome(cur):
                    p.append(cur)
                    backtrack(i+1, p)
                    p.pop()
    
                
        backtrack(0, [])
        return ans