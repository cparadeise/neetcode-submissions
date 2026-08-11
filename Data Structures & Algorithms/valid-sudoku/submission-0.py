class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize collections of sets to track digits
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subgrid = collections.defaultdict(set) # Key will be (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells represented by a period
                if val == ".":
                    continue
                
                # define the coordinate key for the subgrid
                subgrid_key = (r // 3, c // 3)

                # if the digit already exists in the row, column or subgrid
                # return false (it's invalid)
                if (val in rows[r] or
                    val in cols[c] or
                    val in subgrid[subgrid_key]):
                    return False

                # add the digits to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                subgrid[subgrid_key].add(val)

        return True
