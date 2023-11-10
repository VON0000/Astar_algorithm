import random
from typing import Dict, Tuple, Union


def generate_dataset(num_obstacles: int, grid_size: int) -> Dict[str, Union[None, Tuple[float, float], set]]:
    # Create a dataset with obstacles, start points and target points
    dataset = {
        "obstacles": set(),
        "start": None,
        "goal": None
    }

    # Generate obstacles randomly
    while len(dataset["obstacles"]) < num_obstacles:
        obstacle = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        dataset["obstacles"].add(obstacle)

    # Generate start and target points to ensure they are not obstacles randomly
    while dataset["start"] is None or dataset["start"] in dataset["obstacles"]:
        dataset["start"] = (float(random.randint(0, grid_size - 1)), float(random.randint(0, grid_size - 1)))

    while dataset["goal"] is None or dataset["goal"] in dataset["obstacles"] or dataset["goal"] == dataset["start"]:
        dataset["goal"] = (float(random.randint(0, grid_size - 1)), float(random.randint(0, grid_size - 1)))

    return dataset
