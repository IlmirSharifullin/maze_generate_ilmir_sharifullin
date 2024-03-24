import random
from maze_cell import MazeCell


def find(x: MazeCell) -> MazeCell:
    if x.component != x:
        x.component = find(x.component)
    return x.component


def union(x: MazeCell, y: MazeCell):
    root_x: MazeCell = find(x)
    root_y: MazeCell = find(y)
    root_x.component = root_y


def generate_maze(n) -> list[list[MazeCell]]:
    maze = [[MazeCell(x, y) for x in range(n)] for y in range(n)]

    for row in maze:
        for cell in row:
            cell.component = cell

    while any(find(cell) != find(maze[0][0]) for row in maze for cell in row):
        cell: MazeCell = random.choice(random.choice(maze))
        neighbor: tuple[int, int] = random.choice((
            (cell.x, cell.y - 1),
            (cell.x + 1, cell.y),
            (cell.x, cell.y + 1),
            (cell.x - 1, cell.y)
        ))
        if not (0 <= neighbor[0] < n and 0 <= neighbor[1] < n):
            continue

        neighbor_cell = maze[neighbor[1]][neighbor[0]]
        if find(cell) == find(neighbor_cell):
            continue

        union(cell, neighbor_cell)
        if neighbor[0] == cell.x + 1:
            cell.walls[1] = False
            neighbor_cell.walls[3] = False
        elif neighbor[1] == cell.y + 1:
            cell.walls[2] = False
            neighbor_cell.walls[0] = False
        elif neighbor[0] == cell.x - 1:
            cell.walls[3] = False
            neighbor_cell.walls[1] = False
        elif neighbor[1] == cell.y - 1:
            cell.walls[0] = False
            neighbor_cell.walls[2] = False

    for cell in maze[0]:
        cell.walls[0] = True
    for cell in maze[n-1]:
        cell.walls[2] = True
    for i in range(n):
        maze[i][0].walls[3] = True
        maze[i][n-1].walls[1] = True

    maze[0][0].is_open = True
    maze[n - 1][n - 1].is_open = True

    return maze

