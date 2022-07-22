class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = Counter(nums)
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for n in count:
                if count[n] > 0:
                    path.append(n)
                    count[n] -= 1
                    backtrack(path)
                    path.pop()
                    count[n] += 1
                
        backtrack([])
        return ans