class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isDuplicates(counter):
            for char, freq in counter.most_common():
                if char != "." and freq > 1:
                    return True
                
            return False
        
        #for row
        for swi in range(len(board)):
            # print(f"row {swi+1}: {board[swi]} set: {set(board[swi])}")
            counter = collections.Counter(board[swi])
            if isDuplicates(counter):
                return False
            
        
        #for columns
        n_col = len(board[0])
        for swj in range(n_col):
            counter = collections.Counter([row[swj] for row in board])
            if isDuplicates(counter):
                return False
        
        #for 3x3 sub-boxes
        n_row = len(board)
        
        for swi in range(0, n_row, 3):
            for swj in range(0, n_col, 3):
                elements = []
                for swk in range(swi, swi+3):
                    for swl in range(swj, swj+3):
                        elements.append(board[swk][swl])
                
                counter = collections.Counter(elements)
                if isDuplicates(counter):
                    return False
                
        return True
        

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.