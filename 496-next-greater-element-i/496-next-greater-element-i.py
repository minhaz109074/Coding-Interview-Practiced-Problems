class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        nextG = defaultdict(int)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextG[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
            nextG[nums2[i]] = -1
        for j in range(len(nums1)):
            ans[j] = nextG[nums1[j]]
            
        return ans
            