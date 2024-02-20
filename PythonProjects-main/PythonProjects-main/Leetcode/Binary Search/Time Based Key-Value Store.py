class TimeMap:

    def __init__(self):
        self.timemp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemp:
            self.timemp[key] += [(value, timestamp)]
        else:
            self.timemp[key] = [(value, timestamp)]
        return

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.timemp:
            l,r = 0, len(self.timemp[key])-1
            while l <= r:
                mid = (l+r)//2
                if self.timemp[key][mid][-1] == timestamp:
                    return self.timemp[key][mid][0]
                elif self.timemp[key][mid][-1] > timestamp:
                    r = mid -1
                else:
                    res = self.timemp[key][mid][0]
                    l = mid +1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)