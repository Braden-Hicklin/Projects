class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        size = len(nums1)+len(nums2)
        hf = size // 2
        
        # ensure the smaller list is always A
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            # left endpoint for A
            i = (l+r) // 2 
            # left endpoint for B
            j = hf - i - 2   

            # Conditions for edgecases
            Al = A[i] if i >= 0 else float("-infinity")
            Ar = A[i+1] if (i+1) < len(A) else float("infinity")
            Bl = B[j] if j >= 0 else float("-infinity")
            Br = B[j+1] if (j+1) < len(B) else float("infinity")

            # left endpoints were set properly
            if Al <= Br and Bl <= Ar:
                # odd
                if size % 2:
                    return min(Ar, Br)
                # even
                return (max(Al, Bl) + min(Ar, Br))/2
            
            # left endpoints were not set properly
            elif Al > Br:
                r = i -1
            else:
                l = i +1