import matplotlib.pyplot as plt
import numpy as np
from dummy_model import (
    clean_NA,
    read_training_dataset,
)


def make_box_diagram():
    clean_df = clean_NA(read_training_dataset(), 0)
    # Creating figure w/ two subplots
    fig, axs = plt.subplots(1, 2)
    sub_plot_1 = axs[0].boxplot(clean_df["target"])
    axs[0].set_title("Días")
    plt.setp(sub_plot_1["boxes"], color="red")
    plt.setp(sub_plot_1["whiskers"], color="red")
    axs[0].yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)

    sub_plot_2 = axs[1].boxplot(clean_df["Masa"])
    axs[1].set_title("Masa")
    plt.setp(sub_plot_2["boxes"], color="blue")
    plt.setp(sub_plot_2["whiskers"], color="blue")
    axs[1].yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)

    plt.savefig("images/Box_diagram_train.png")

    return axs
