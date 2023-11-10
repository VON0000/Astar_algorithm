import random
from typing import Dict, Tuple, Union


def generate_dataset(num_obstacles: int, grid_size: int) -> Dict[str, Union[None, Tuple[float, float], set]]:
    # 创建一个包含障碍物、起始点和目标点的数据集
    dataset = {
        "obstacles": set(),
        "start": None,
        "goal": None
    }

    # 随机生成障碍物
    while len(dataset["obstacles"]) < num_obstacles:
        obstacle = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        dataset["obstacles"].add(obstacle)

    # 随机生成起始点和目标点，确保它们不是障碍物
    while dataset["start"] is None or dataset["start"] in dataset["obstacles"]:
        dataset["start"] = (float(random.randint(0, grid_size - 1)), float(random.randint(0, grid_size - 1)))

    while dataset["goal"] is None or dataset["goal"] in dataset["obstacles"] or dataset["goal"] == dataset["start"]:
        dataset["goal"] = (float(random.randint(0, grid_size - 1)), float(random.randint(0, grid_size - 1)))

    return dataset
