import copy

from matplotlib import pyplot as plt, patches


def environment_plot(dataset: dict, grid_size: int):
    fig, ax = plt.subplots()

    # Set the grid size
    ax.set_xlim([0, grid_size])
    ax.set_ylim([0, grid_size])

    # add obstacles squares
    for x in range(grid_size):
        for y in range(grid_size):
            if (x, y) in dataset["obstacles"]:
                square = patches.Rectangle((x, y), 1, 1, fill=True, color='tomato')
                ax.add_patch(square)
    plot_dataset = copy.deepcopy(dataset)
    add_to_floats(plot_dataset)
    plt.scatter(*plot_dataset["start"], marker='o', color='chartreuse', label='Start', s=40)
    plt.scatter(*plot_dataset["goal"], marker='*', color='dodgerblue', label='Goal', s=40)


def draw_grid_origin(dataset: dict, grid_size: int):
    environment_plot(dataset, grid_size)
    plt.show()


def plot_grid(dataset: dict, path: list, grid_size: int):
    environment_plot(dataset, grid_size)
    plot_path = copy.deepcopy(path)
    plot_path = [(item[0] + 0.5, item[1] + 0.5) for item in plot_path]
    plt.plot(*zip(*plot_path), color='black', label='Path', linewidth=1.0)
    plt.title('A* Algorithm Result')
    plt.show()


def add_to_floats(plot_dataset: dict):
    for key, value in plot_dataset.items():
        if isinstance(value, tuple) and all(isinstance(item, float) for item in value):
            # if the value is a tuple, update each float in the tuple
            plot_dataset[key] = tuple(item + 0.5 for item in value)
        elif isinstance(value, set):
            # if the value is a set, update each float in the set
            new_set = set()
            for item in value:
                if isinstance(item, float):
                    new_set.add(item + 0.5)
                else:
                    new_set.add(item)
            plot_dataset[key] = new_set
