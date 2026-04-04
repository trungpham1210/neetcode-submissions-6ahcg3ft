class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row wise condition:
        for r in range(9):
            seen = set()
            for c in range(9):
                e = board[r][c]
                if e == ".": continue
                if e in seen:
                    return False
                seen.add(e)
        #check column wise condition
        for c in range(9):
            seen = set()
            for r in range(9):
                e = board[r][c]
                if e == ".": continue
                if e in seen:
                    return False
                seen.add(e)
        #check square wise condition
        for big_row in range(0, 9, 3):
            for big_col in range(0, 9, 3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        #if the current e is seen, return false
                        e = board[big_row + r][big_col + c]
                        if e == ".": continue
                        if e in seen:
                            return False
                        #else mark it as seen
                        seen.add(e)
        return True


