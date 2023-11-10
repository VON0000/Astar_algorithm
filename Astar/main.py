from getdata import generate_dataset
from plot import draw_grid_origin, plot_grid


def heuristic(node: tuple, goal: tuple) -> float:
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(point: tuple) -> list:
    x, y = point
    neighbors = []

    # 检查上方邻居
    if y > 0:
        neighbors.append((x, y - 1))

    # 检查下方邻居
    if y < 9:
        neighbors.append((x, y + 1))

    # 检查左边邻居
    if x > 0:
        neighbors.append((x - 1, y))

    # 检查右边邻居
    if x < 9:
        neighbors.append((x + 1, y))

    return neighbors


def a_star(start: tuple, goal: tuple, obstacles: set) -> list:
    open_list = [start]
    closed_list = []
    g = {start: 0}
    parents = {start: start}

    while len(open_list) > 0:
        current = min(open_list, key=lambda x: g[x] + heuristic(x, goal))

        if current == goal:
            path = []
            while parents[current] != current:
                path.append(current)
                current = parents[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in get_neighbors(current):
            if (neighbor in closed_list) or (neighbor in obstacles):
                continue
            tentative_g_score = g[current] + 1

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_score >= g[neighbor]:
                continue

            parents[neighbor] = current
            g[neighbor] = tentative_g_score

    return []


if __name__ == '__main__':
    grid_size = 10  # Set grid size
    num_obstacles = 25  # Total number of obstacles
    dataset = generate_dataset(num_obstacles, grid_size)
    draw_grid_origin(dataset)
    path = a_star(dataset["start"], dataset["goal"], dataset["obstacles"])
    plot_grid(dataset, path)