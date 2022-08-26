class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set = set()
        board_size = len(board)
        for row in range(board_size):
            for col in range(board_size):
                curr_cell = board[row][col]
                if curr_cell == ".":
                    continue
                row_repr = f"{curr_cell} in row {row}"
                col_repr = f"{curr_cell} in col {col}"
                subbox_repr = f"{curr_cell} in box {row//3}-{col//3}"
                
                for _repr in [row_repr, col_repr, subbox_repr]:
                    if _repr in hash_set:
                        return False
                    hash_set.add(_repr)
                    
        return True