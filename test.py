# Desc: 测试文件
from matplotlib import pyplot as plt

from getdata import generate_dataset
from main import get_neighbors
from plot import add_to_floats


def test_get_neighbors():
    # 示例
    point = (5, 5)
    neighbors = get_neighbors(point)
    print(neighbors)


def test_generate_dataset():
    # 生成数据集
    grid_size = 10  # 设定网格大小
    num_nodes = 32  # 总节点数
    dataset = generate_dataset(num_nodes, grid_size)

    # 绘制数据集
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
