class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perms(res, a, l, r):
            if l == r:
                res.append(a[:])
            else:
                for i in range(l, r):
                    a[l], a[i] = a[i], a[l]
                    perms(res, a, l+1, r)
                    a[l], a[i] = a[i], a[l]
            return res
        a = nums
        r = len(a)
        res = []
        return perms(res, a, 0, r)