class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = ''.join(sorted(s))
        j = ''.join(sorted(t))
        if i != j:
            return False
        else:
            return True

# Sorts the two strings and compares
# Sorted returns a list so ''.join is used to convert back into a string (not necessary for return)