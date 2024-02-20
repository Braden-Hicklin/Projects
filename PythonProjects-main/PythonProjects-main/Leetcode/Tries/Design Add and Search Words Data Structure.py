class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end = 'end' 

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            
        node[self.end] = True

    def dfs(self, word, idx, node):
        if idx == len(word):
            return self.end in node
        if word[idx] == '.':
            for nc in node:
                if nc != self.end:
                    found = self.dfs(word, idx +1, node[nc])
                    if found:
                        return True
        else:
            if word[idx] in node:
                return self.dfs(word, idx + 1, node[word[idx]])
        return False

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)  