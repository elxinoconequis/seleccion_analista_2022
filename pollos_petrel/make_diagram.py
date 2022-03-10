import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_box_diagram(clean_df: pd.DataFrame):
    fig, axs = plt.subplots(1, 2)
    plot_first_subplot(clean_df, axs, 0)
    plot_second_subplot(clean_df, axs, 1)
    save_figure()
    return axs


# Hacer primer subplot
def plot_first_subplot(clean_df: pd.DataFrame, axs: np.ndarray, index: int):
    sub_plot_1 = axs[index].boxplot(clean_df["target"])
    axs[index].set_title("Días")
    plt.setp(sub_plot_1["boxes"], color="red")
    plt.setp(sub_plot_1["whiskers"], color="red")
    make_grid_first_subplot(axs, index)


# Hacer segundo subplot
def plot_second_subplot(clean_df: pd.DataFrame, axs: np.ndarray, index: int):
    sub_plot_2 = axs[index].boxplot(clean_df["Masa"])
    axs[index].set_title("Masa")
    plt.setp(sub_plot_2["boxes"], color="blue")
    plt.setp(sub_plot_2["whiskers"], color="blue")
    make_grid_second_subplot(axs, index)


# Hacer lineas grid de un subplot color gris tenue para primer subplot
def make_grid_first_subplot(axs: np.ndarray, index: int):
    axs[index].yaxis.grid(
        linestyle="-", which="major", color="lightgrey", alpha=0.5
    )  # Si hay otros argumentos, la función asume un True


# Hacer lineas grid de un subplot color gris tenue para segundo subplot
def make_grid_second_subplot(axs: np.ndarray, index: int):
    axs[index].yaxis.grid(linestyle="-", which="major", color="lightgrey", alpha=0.5)


# Guardar figura
def save_figure():
    plt.savefig("images/Box_diagram_train.png")
