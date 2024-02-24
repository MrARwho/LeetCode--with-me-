import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqar = collections.defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows or 
                    board[i][j] in cols or
                    board[i][j] in sqar[(i//3 , j//3)]):
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                sqar[(i//3 , j//3)].add(board[i][j])
                
        # print(rows)
        # print(cols)
                
        return True
                    
    

a = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# board[0].remove('5')
# print(board[0])
# # print(board)
print(a.isValidSudoku(board))