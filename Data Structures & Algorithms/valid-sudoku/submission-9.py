class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        b = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]

                if val != '.':

                    board_idx = ((row // 3) * 3 + (col // 3))
                    
                    if(
                        val in cols[col] or
                        val in rows[row] or
                        val in b[board_idx]
                    ):
                        return False
                
                

                    cols[col].add(val)
                    b[board_idx].add(val)
                    rows[row].add(val)
      
        return True
    
        