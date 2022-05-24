class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordcount = Counter(words)
        heap = [(-freq,word)  for word, freq in wordcount.items()] # max heap
        heapq.heapify(heap)
        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        return ans