class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = []
        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                ans[stack[-1]] = nums[i%n]
                stack.pop()
            stack.append(i%n)
        
        return ans