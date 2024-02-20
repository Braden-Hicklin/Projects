class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i not in temp:
                temp[i] = {}
            temp = temp[i]
        temp['end'] = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i not in temp:
                return False
            temp = temp[i]
        if 'end' in temp:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i not in temp:
                return False
            temp = temp[i]
        return True


# ADDITIONAL MORE COMPLEX CODE
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:

    def __init__(self):      
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charIdx(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word: str) -> None:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charIdx(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEnd = True

    def search(self, word: str) -> bool:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charIdx(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEnd

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        length = len(prefix)
        for level in range(length):
            index = self.charIdx(prefix[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return True