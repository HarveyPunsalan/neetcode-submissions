from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)     # rows[0] = numbers seen in row 0
        cols = defaultdict(set)     # cols[3] = numbers seen in column 3
        squares = defaultdict(set)  # squares[(0,0)] = numbers in top-left box

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":       # empty cell, skip it
                    continue

                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False     # duplicate found!

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
        