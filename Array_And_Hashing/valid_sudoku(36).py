import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(list)
        rows = collections.defaultdict(list)
        sqar = collections.defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or
                    board[i][j] in sqar[(i//3 , j//3)]):
                    return False
                cols[j].append((board[i][j]))
                rows[i].append(board[i][j])
                sqar[(i//3 , j//3)].append(board[i][j])
                
        # print(rows)
        # print(cols)
                
        return True
                    
    

a = Solution()
board =[[".",".","4",".",".",".","6","3","."],
        [".",".",".",".","6",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".",".","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
# board[0].remove('5')
# print(board[0])
# # print(board)
print(a.isValidSudoku(board))