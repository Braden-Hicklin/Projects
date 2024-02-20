class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # DFS to recursively traverse the board searching for words
        def dfs(x, y, root):
            char = board[x][y]
            currNode = root[char]
            # check if the node has word in it
            word = currNode.pop('#', False)
            # if the word is found add it to solution
            if word:
                res.append(word)
            
            # mark as visited
            board[x][y] = '*'
            # recursion
            for dirX, dirY in [(0,1), (0,-1), (1,0), (-1,0)]:
                currX, currY = x + dirX, y + dirY
                if 0 <= currX < m and 0 <= currY < n and board[currX][currY] in currNode:
                    dfs(currX, currY, currNode)
            # set the value of the current position back to normal
            board[x][y] = char
            # if the current node has no children then remove from trie
            if not currNode:
                root.pop(char)

        # create Trie
        trie = dict()
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        
        # get the board size
        m, n = len(board), len(board[0])
        res = []

        # traverse board 
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res