import copy

from matplotlib import pyplot as plt, patches


def draw_grid_origin(dataset: dict):
    fig, ax = plt.subplots()

    # 设置网格大小
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    # 添加正方形
    for x in range(10):
        for y in range(10):
            if (x, y) in dataset["obstacles"]:
                square = patches.Rectangle((x, y), 1, 1, fill=True, color='tomato')
                ax.add_patch(square)
    plot_dataset = copy.deepcopy(dataset)
    add_to_floats(plot_dataset)
    plt.scatter(*plot_dataset["start"], marker='o', color='chartreuse', label='Start', s=40)
    plt.scatter(*plot_dataset["goal"], marker='*', color='dodgerblue', label='Goal', s=40)
    plt.show()


def plot_grid(dataset: dict, path: list):
    fig, ax = plt.subplots()

    # 设置网格大小
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    # 添加正方形
    for x in range(10):
        for y in range(10):
            if (x, y) in dataset["obstacles"]:
                square = patches.Rectangle((x, y), 1, 1, fill=True, color='tomato')
                ax.add_patch(square)
    plot_dataset = copy.deepcopy(dataset)
    plot_path = copy.deepcopy(path)
    plot_path = [(item[0] + 0.5, item[1] + 0.5) for item in plot_path]
    add_to_floats(plot_dataset)
    plt.scatter(*plot_dataset["start"], marker='o', color='chartreuse', label='Start', s=40)
    plt.scatter(*plot_dataset["goal"], marker='*', color='dodgerblue', label='Goal', s=40)
    plt.plot(*zip(*plot_path), color='black', label='Path', linewidth=1.0)
    plt.title('A* Algorithm Result')
    plt.show()


def add_to_floats(plot_dataset: dict):
    for key, value in plot_dataset.items():
        if isinstance(value, tuple) and all(isinstance(item, float) for item in value):
            # 如果值是一个浮点数元组
            plot_dataset[key] = tuple(item + 0.5 for item in value)
        elif isinstance(value, set):
            # 如果值是一个集合，更新集合中的每个浮点数
            new_set = set()
            for item in value:
                if isinstance(item, float):
                    new_set.add(item + 0.5)
                else:
                    new_set.add(item)
            plot_dataset[key] = new_set
