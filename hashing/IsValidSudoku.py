class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if (f"{num} in row{i}" in seen or
                        f"{num} in col{j}" in seen or
                        f"{num} in box{i//3}-{j//3}" in seen):
                        return False
                    seen.add(f"{num} in row{i}")
                    seen.add(f"{num} in col{j}")
                    seen.add(f"{num} in box{i//3}-{j//3}")
        return True


# Sample test board (valid partial Sudoku)
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board))  # Should print True
