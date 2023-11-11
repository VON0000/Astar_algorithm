from Astar.getdata import generate_dataset
from Astar.plot import draw_grid_origin, plot_grid


def heuristic(node: tuple, goal: tuple) -> float:
    """
    Calculate the heuristic value of a node by using the Euclidean distance
    Attention: use math module by "import math"
    :param node: the current node
    :param goal: the goal node
    :return: the heuristic value

    >>> heuristic((0,0), (1,1))
    1.4142135623730951
    >>> heuristic((0,0), (2,2))
    2.8284271247461903
    >>> heuristic((0,0), (0,0))
    0.0
    """


def get_neighbors(point: tuple) -> list:
    """
    Get the neighbors of a point in the grid
    :param point: a set of coordinates
    :return: the list of neighbors

    >>> (0,1) in get_neighbors((1,1))
    True
    >>> (0,0) in get_neighbors((1,1))
    False
    >>> (2,2) in get_neighbors((1,1))
    False
    >>> (8,8) in get_neighbors((9,9))
    False
    >>> (9,8) in get_neighbors((9,9))
    True
    >>> (8,9) in get_neighbors((9,9))
    True
    >>> (9,9) in get_neighbors((9,9))
    False
    """


def get_current_node(open_list: list, g: dict, goal: tuple) -> tuple:
    """
    Get the current node from the open list
    :param open_list: the list of nodes to be explored
    :param g: the cost to reach the current node
    :param goal: the goal node
    :return: the current node

    >>> get_current_node([(0,0),(1,1)], {(0,0):0, (1,1):1}, (2,2))
    (1, 1)
    >>> get_current_node([(3,4), (5,7)], {(3,4):2, (5,7):5}, (8,8))
    (5, 7)
    >>> get_current_node([(0,0), (9,9), (5,5)], {(0,0):0, (9,9):9, (5,5):4}, (6,6))
    (5, 5)
    >>> get_current_node([(2,3), (7,4)], {(2,3):3, (7,4):6}, (7,7))
    (7, 4)
    """


def get_path(parents: dict, start: tuple, current: tuple) -> list:
    """
    Get the path from the start node to the goal node
    :param parents:  the dictionary of parents
    :param start:  the start node
    :param current:  the goal node
    :return:  the path from the start node to the goal node

    >>> get_path({(0,0):(0,0), (1,1):(0,0), (2,2):(1,1)}, (0,0), (2,2))
    [(0, 0), (1, 1), (2, 2)]
    >>> get_path({(0,0):(0,0), (1,1):(0,0), (2,2):(1,1)}, (0,0), (1,1))
    [(0, 0), (1, 1)]
    >>> get_path({(0,0):(0,0), (1,1):(0,0), (2,2):(1,1)}, (0,0), (0,0))
    [(0, 0)]
    """


def a_star(start: tuple, goal: tuple, obstacles: set) -> list:
    open_list = [start]
    closed_list = []
    g = {start: 0}
    parents = {start: start}

    while len(open_list) > 0:
        current = get_current_node(open_list, g, goal)

        if current == goal:
            return get_path(parents, start, current)

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in get_neighbors(current):
            if ...:  # TODO: Determine if the current neighbor needs to be skipped
                continue
            tentative_g_score = g[current] + 1

            if neighbor not in open_list:
                ...  # TODO: add neighbor to open list
            elif ...:  # TODO: Determine if the tentative g score is greater than the g score of the neighbor
                continue

            parents[neighbor] = current
            g[neighbor] = tentative_g_score

    return []


if __name__ == '__main__':
    grid_size = 10  # Set grid size
    num_obstacles = 25  # Total number of obstacles
    dataset = generate_dataset(num_obstacles, grid_size)
    draw_grid_origin(dataset, grid_size)
    path = a_star(dataset["start"], dataset["goal"], dataset["obstacles"])
    plot_grid(dataset, path, grid_size)
