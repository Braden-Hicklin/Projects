class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if len(t) > len(s):
            return ""
        l = 0
        res = (0, float('inf'))
        need = len(t)
        needMap = collections.defaultdict(int)
        for c in t:
            needMap[c] += 1
        for r in range(len(s)):
            if needMap[s[r]] > 0:
                need -= 1
            needMap[s[r]] -= 1
            if need == 0:
                while True:
                    tmp = s[l]
                    if needMap[tmp] == 0:
                        break
                    needMap[tmp] += 1
                    l += 1   
                if r - l < res[1] - res[0]:
                    res = (l, r)
                needMap[s[l]] += 1
                need += 1
                l += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]