class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 3 conditions

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        bo = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                
                block_idx = (row // 3) * 3 + (col // 3)

                if (val in rows[row] or
                    val in cols[col] or
                    val in bo[block_idx]):
                    return False

                rows[row].add(val)
                cols[col].add(val)
                bo[block_idx].add(val)
                
        return True
        