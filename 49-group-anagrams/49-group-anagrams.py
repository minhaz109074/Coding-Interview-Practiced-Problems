class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for st in strs:
            sts = ''.join(sorted(st))
            s[sts].append(st)
        
        return s.values()