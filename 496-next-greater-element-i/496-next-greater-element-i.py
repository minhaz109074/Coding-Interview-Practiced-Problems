class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextG = defaultdict(int)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextG[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
            nextG[nums2[i]] = -1
            
        return [nextG[v] for v in nums1]
            