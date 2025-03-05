from time import time

def backtracking(sudoku):
    start = time()
    grid = sudoku.grid

    empty_spaces = []
    for i in range(sudoku.n):
        for j in range(sudoku.n):
            if not grid[i][j]:
                options = sudoku.cell_options((i, j))
                if len(options) == 1:
                    grid[i][j] = options[0]
                else:
                    empty_spaces.append((i, j))

    index = 0
    tried = {}
    while not sudoku.is_complete():
        i, j = empty_spaces[index][0], empty_spaces[index][1]
        options = sudoku.cell_options((i, j))
        if (i, j) in tried:
            options = list(set(options).difference(tried[(i, j)]))
        if not options:
            index -= 1
            tried[(i, j)] = []
            grid[empty_spaces[index][0]][empty_spaces[index][1]] = 0
        else:
            value = options[0]
            grid[i][j] = value
            if (i, j) not in tried:
                tried[(i, j)] = [value]
            else:
                tried[(i, j)] += [value]
            index += 1

    print(f'solve time: {(time() - start):.4f}s')
    return grid
