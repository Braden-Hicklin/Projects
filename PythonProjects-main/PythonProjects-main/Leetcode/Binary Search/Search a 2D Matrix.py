class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        for li in matrix:
            flag = self.binarySearch(li, l, r, target)
            if flag == True:
                return True
        return False

    def binarySearch(self, li, l, r, x):
        if r >= l:
            mid = (r+l) // 2
            if li[mid] == x:
                return True
            elif li[mid] > x:
                return self.binarySearch(li, l, mid - 1, x)
            else:
                return self.binarySearch(li, mid + 1, r, x)
        else:
            return False