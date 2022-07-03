class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            l, r = 0, len(self.map[key])
            while l < r:
                mid = (l + r) >> 1
                if timestamp >= self.map[key][mid][0] :
                    l = mid + 1
                else:
                    r = mid
            return self.map[key][r-1][1] if r != 0 else ""
                
        return "" 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)