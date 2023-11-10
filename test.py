# Desc: Test file for A* algorithm
from matplotlib import pyplot as plt

from Astar.getdata import generate_dataset
from Astar.main import get_neighbors, get_current_node, heuristic, get_path
from Astar.plot import add_to_floats


def test_get_neighbors():
    point = (5, 5)
    neighbors = get_neighbors(point)
    print(neighbors)


def test_generate_dataset():
    grid_size = 10
    num_nodes = 32
    dataset = generate_dataset(num_nodes, grid_size)

    # Plot the dataset
    plt.figure(figsize=(10, 10))
    plt.scatter(*zip(*dataset["obstacles"]), marker='X', color='red', label='Obstacles')
    plt.scatter(*dataset["start"], marker='o', color='green', label='Start')
    plt.scatter(*dataset["goal"], marker='*', color='blue', label='Goal')
    plt.title('A* Algorithm Dataset')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_add_to_floats():
    example_dict = {
        "a": (1.0, 2.0),
        "b": None,
        "c": {3.5, "hello", 4.0},
        "d": (5.5, 6.5)
    }

    add_to_floats(example_dict)
    print(example_dict)


def test_get_current_node():
    # [(0,0),(1,1)], {(0,0):0, (1,1):1}, (2,2)
    open_list = [(0, 0), (1, 1)]
    g = {(0, 0): 0, (1, 1): 1}
    goal = (2, 2)
    current = get_current_node(open_list, g, goal)
    print(current)


def test_heuristic():
    # (0,0), (1,1)
    node = (0, 0)
    goal = (1, 1)
    h = heuristic(node, goal)
    print(h)


def test_get_path():
    # {(0,0):(0,0), (1,1):(0,0), (2,2):(1,1)}, (0,0), (1,1)
    parents = {(0, 0): (0, 0), (1, 1): (0, 0), (2, 2): (1, 1)}
    start = (0, 0)
    current = (1, 1)
    path = get_path(parents, start, current)
    print(path)
