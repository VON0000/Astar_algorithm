# Desc: 测试文件
from matplotlib import pyplot as plt

from getdata import generate_dataset
from main import get_neighbors
from plot import add_to_floats


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
