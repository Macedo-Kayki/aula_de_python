import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

def generate_data(n:int, seed:int|None=123) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.random((n, n))

def process_data(data: np.ndarray) -> float:
    data_squared = data @ data
    return float(data_squared.mean())


def plot_data(data: np.ndarray) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(4, 3))
    im = ax.imshow(data, cmap="viridis")
    fig.colorbar(im, ax=ax)
    ax.set_title("mapa de calor")
    return fig, ax

if __name__ == "__main__":
    mat = generate_data(77, seed=777)
    metric = process_data(mat)
    fig, ax = plot_data(mat)
    fig.savefig("heatmap.png", dpi=120)
    print(f"Métrica={metric:.6f}")