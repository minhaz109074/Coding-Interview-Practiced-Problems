class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = [[] for i in range(len(words)+1)]
        for key,val in Counter(words).items():
            freq[val].append(key)
        ans = []
        for i in reversed(range(len(words)+1)):
            for st in sorted(freq[i]):
                ans.append(st)
                if len(ans) == k: return ans