class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        product = 1
        zeroChk = nums.count(0)
        for i in nums:
            if zeroChk == 1:
                if i != 0:
                    product *= i
            else:
                product *= i
        for i in nums:
            if zeroChk == 1:
                if i == 0:
                    solution.append(product)
                else:
                    solution.append(0)
            elif zeroChk > 1:
                solution.append(0)
            else:
                solution.append(int(product/i))
        return solution

# Uses arrays and list comprehension (count) to get the product of all integers in list while
# ensuring the calculation doesn't cause problems when computing zeros