from sudokuSolveAlgorithms import backtracking

class Sudoku:
    """Instantiate and solve (9x9) sudoku puzzles."""
    n = 9
    cell_type = int
    optns_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, grid):
        """Instantiate a sudoku grid."""
        if isinstance(grid, str):
            self.grid = []
            for i in range(self.n):
                temp = []
                for j in range(self.n):
                    temp.append(self.cell_type(grid[i*self.n + j]))
                self.grid.append(temp)
        elif isinstance(grid, list):
            self.grid = grid
        else: raise NotImplementedError(f'grid of type {type(grid)} not implemented.')

    def cell_options(self, position):
        """Return a list of valid inputs to the cell at a given position."""
        grid = self.grid
        row = position[0]
        column = position[1]

        seen_set = set(grid[row])

        for i in range(self.n):
            seen_set.add(grid[i][column])

        for i in range(3*(row//3), 3*(row//3) + 3):
            for j in range(3*(column//3), 3*(column//3) + 3):
                seen_set.add(grid[i][j])

        return list(self.optns_set.difference(seen_set))

    def is_complete(self):
        """Check if the sudoku grid is complete i.e. has no empty squares."""
        for i in range(self.n):
            for j in range(self.n):
                if not self.grid[i][j]:
                    return False
        return True

    @property
    def show(self):
        """Print the Sudoku in a readable form."""
        grid = self.grid
        for i in range(9):
            line = ""
            if i == 3 or i == 6:
                print("---------------------")
            for j in range(9):
                if j == 3 or j == 6:
                    line += "| "
                line += str(grid[i][j])+" "
            print(line)

    def solve(self, algorithm=backtracking):
        """Solve the sudoku grid via a specified algorithm."""
        grid = algorithm(self)
        return Sudoku(grid)
        


if __name__ == "__main__":
    # Example Usage:
    # grid1 and grid2 are equivalent.
    grid1 = [
    [0,0,2,0,0,8,0,0,9],
    [7,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,3,0,6,0],
    [2,0,6,0,0,0,0,0,0],
    [0,4,0,0,1,0,7,0,0],
    [0,0,0,9,6,0,0,0,0],
    [9,1,0,0,0,0,0,0,7],
    [0,8,0,0,0,0,0,5,0],
    [4,0,0,0,8,0,9,0,0]
    ]
    grid2 = '002008009700000000000043060206000000040010700000960000910000007080000050400080900'
    s = Sudoku(grid2)
    s.solve().show
