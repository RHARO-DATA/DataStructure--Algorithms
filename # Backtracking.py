# Backtracking

maze = [[".",".",".","."],
        [".","x","x","x"]
        [".",".",".","x"]
        ["x","x",".","."]]

def print_maze(maze)
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)

def solve_maze(maze):
    # your code
    if len (maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    return solve_maze_helper(maze,[], 0, 0)

def solve_maze_helper(meze, sol, pos_row, pos_col):
    # Get size of the maze
    num_row = len(maze)
    num_col = len maze[0]

    # Base Case
    #Robot already home
    if pos_row == num_row -1 and pos_col == num_col -1:
        return sol

    # Out of Bounds
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # Is an obstacle
    if maze[pos_row][pos_col] == 'x'

    # Recursive Case

    # Try to going Right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col +1)
    if sol_going_right is not None:
        return sol_going_right

    # Going right doen't work, backtrack, try going down
    sol.pop()
    sol.append('d')
    sol_going_down = solve_maze_helper(maze, sol, pos_row +1, pos_col)
    if sol_going_down if not None:
        return sol_going_down

    # No solution, imposible, backtracking
    sol.pop()
    return None

    




    
