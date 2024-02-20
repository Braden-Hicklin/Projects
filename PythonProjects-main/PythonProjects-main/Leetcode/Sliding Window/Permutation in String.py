class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, val, chkVal = 0, 1, 1
        for i in s1: val *= ord(i)

        for r in range(len(s2)):
            chkVal *= ord(s2[r])
            if (r-l+1) == len(s1):
                if chkVal == val:
                    return True
                chkVal = chkVal // ord(s2[l])
                l +=1
        return False      