from sudoku import sudoku

class GiantSudoku(sudoku):
    """Implements a 25x25 sudoku grid, with cell values A-Y"""
    n = 25
    cell_type = str
    optns_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'}
    # Requires new implementation of 'cell_options', 'solve', 'show'
    def __init__(self, grid):
        super().__init__(grid)

if __name__ == '__main__':
    pass
