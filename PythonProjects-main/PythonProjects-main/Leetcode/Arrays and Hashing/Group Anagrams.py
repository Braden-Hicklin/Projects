class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anMap = {}
        solution = []
        word = ""
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word not in anMap:
                anMap[word] = [strs[i]]
            else:
                anMap[word] += [strs[i]]
        for i in anMap.values():
            solution.append(list(map(lambda x: x, i)))
        return solution

# Uses hash map to store each word by its sorted key