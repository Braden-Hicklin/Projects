class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = dict()
        rowMap = dict()
        gridMap = dict()
        gridex = str()
        key = str()
        for i in range(len(board)):
            for j, k in enumerate(board[i]):
                if k != ".":
                    key = k
                    gridex = str(j//3) + str(i//3)
                    if key in colMap:
                        if j in colMap[key] or i in rowMap[key]:
                            return False
                        colMap[key] += [j]
                        rowMap[key] += [i]
                    else:
                        colMap[key] = [j]
                        rowMap[key] = [i]
                    if gridex in gridMap:
                        if k in gridMap[gridex]:
                            return False
                        gridMap[gridex] += [k]
                    else:
                        gridMap[gridex] = [k]              
        return True