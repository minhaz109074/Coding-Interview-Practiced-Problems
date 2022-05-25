class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        heap = [(-val, key) for key, val in Counter(s).items()]
        heapq.heapify(heap)
        for k in range(len(heap)):
            freq, key = heapq.heappop(heap)
            for i in range(-freq):
                ans += key
        return ans