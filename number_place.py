# global constant
NUMBERS = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )

def generate_grid():
    return [ [ None for j in range(9) ] for i in range(9) ]

def readfile(filename):
    infile = open(filename, 'r')
    rows = [ row.strip().split(',') for row in infile.readlines() ]
    infile.close()
    grid = [ [ int(col) if col != '' else None for col in row ] for row in rows ]
    clues = [ (i, j) for i in range(9) for j in range(9) if grid[i][j] ]
    return grid, clues

def display_grid(grid):
    for row in grid:
        print(' '.join([ str(n) if n != None else '_' for n in row ]))

def column(grid, j):
    return [ row[j] for row in grid ]

def box(grid, row, col):
    i, j = 3 * (row // 3), 3 * (col // 3)
    return [grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]

def number_place_p(grid, n, i, j):
    if n not in grid[i] and n not in column(grid, j) and n not in box(grid, i, j):
        return True
    else:
        return False

def empty_cell(grid):
    for i in range(9):
        if None in grid[i]:
            return(i, grid[i].index(None))

def complete_p(grid):
    return sum(row.count(None) for row in grid) == 0

def solve(grid, clues):
    if complete_p(grid):
        return grid
    row, col = empty_cell(grid)
    for number in NUMBERS:
        if number_place_p(grid, number, row, col):
            grid[row][col] = number
            grid = solve(grid, clues)
            if complete_p(grid):
                return grid
            grid[row][col] = None # backtrack
    return grid

