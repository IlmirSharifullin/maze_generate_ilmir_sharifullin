from matplotlib import pyplot as plt

from maze_cell import MazeCell


def draw_maze(maze: list[list[MazeCell]]):
    fig, ax = plt.subplots()

    for row in maze:
        for cell in row:
            if cell.walls[0]:
                ax.plot([cell.x, cell.x + 1], [cell.y, cell.y], 'k-')
            if cell.walls[1]:
                ax.plot([cell.x + 1, cell.x + 1], [cell.y, cell.y + 1], 'k-')
            if cell.walls[2]:
                ax.plot([cell.x, cell.x + 1], [cell.y + 1, cell.y + 1], 'k-')
            if cell.walls[3]:
                ax.plot([cell.x, cell.x], [cell.y, cell.y + 1], 'k-')

            if cell.is_open:
                if cell.x == 0 and cell.y == 0:  # Вход с левого края
                    ax.plot([cell.x, cell.x + 1], [cell.y, cell.y], color='white', linewidth=2)
                if cell.x == len(maze) - 1 and cell.y == len(maze) - 1:  # Выход с правого края
                    ax.plot([cell.x, cell.x + 1], [cell.y + 1, cell.y + 1], color='white', linewidth=2)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
