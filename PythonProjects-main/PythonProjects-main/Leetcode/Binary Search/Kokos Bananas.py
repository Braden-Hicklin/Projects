class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binarySearch(l, r):
            res = r
            while l <= r:
                mid = (l+r)//2
                hours = 0
                for elem in piles:
		    # Round up using math.ceil
                    hours += math.ceil(elem/mid)
                if hours <= h:
                    res = min(res, mid)
                    r = mid - 1
                else:
                    l = mid + 1
            return res
    
        l, r = 1, max(piles)
        result = binarySearch(l, r)
        return result