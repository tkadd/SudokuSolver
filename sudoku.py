from time import time


class Sudoku:
    """Instantiate and solve sudoku puzzles."""

    def __init__(self, grid):
        """Instantiate a sudoku grid."""
        self.grid = grid

    def cell_options(self, position):
        """Return a list of valid inputs to the cell at a given position."""
        grid = self.grid
        row = position[0]
        column = position[1]

        seen_set = set(grid[row])

        for i in range(9):
            seen_set.add(grid[i][column])

        for i in range(3*(row//3), 3*(row//3) + 3):
            for j in range(3*(column//3), 3*(column//3) + 3):
                seen_set.add(grid[i][j])

        return list({1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(seen_set))

    def is_complete(self):
        """Check if the sudoku grid is complete i.e. has no empty squares."""
        for i in range(9):
            for j in range(9):
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

    @property
    def solve(self):
        """Solve the sudoku grid via a backtracking algorithm."""
        start = time()
        grid = self.grid

        empty_spaces = []
        for i in range(9):
            for j in range(9):
                if not grid[i][j]:
                    options = self.cell_options((i, j))
                    if len(options) == 1:
                        grid[i][j] = options[0]
                    else:
                        empty_spaces.append((i, j))

        index = 0
        back_tracks = 0
        tried = {}
        while not self.is_complete():
            i, j = empty_spaces[index][0], empty_spaces[index][1]
            options = self.cell_options((i, j))
            if (i, j) in tried.keys():
                options = list(set(options).difference(tried[(i, j)]))
            if not options:
                tried[(i, j)] = []
                grid[empty_spaces[index - 1][0]][empty_spaces[index - 1][1]]\
                    = 0
                back_tracks += 1
                index -= 1
            else:
                value = options[0]
                grid[i][j] = value
                if (i, j) not in tried.keys():
                    tried[(i, j)] = [value]
                else:
                    tried[(i, j)] += [value]
                index += 1

        print(f'solve time: {(time() - start):.4f}s')
        print(f'mistakes: {back_tracks  }')
        return Sudoku(grid)

# Example usage:

# s = Sudoku([
#     [0,0,2,0,0,8,0,0,9],
#     [7,0,0,0,0,0,0,0,0],
#     [0,0,0,0,4,3,0,6,0],
#     [2,0,6,0,0,0,0,0,0],
#     [0,4,0,0,1,0,7,0,0],
#     [0,0,0,9,6,0,0,0,0],
#     [9,1,0,0,0,0,0,0,7],
#     [0,8,0,0,0,0,0,5,0],
#     [4,0,0,0,8,0,9,0,0]
# ])
# s.solve.show
