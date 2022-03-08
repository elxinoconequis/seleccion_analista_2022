import matplotlib.pyplot as plt
import numpy as np
import os
from pollos_petrel.make_diagram import (
    make_box_diagram,
)

from pollos_petrel.dummy_model import (
    clean_NA,
    read_testing_dataset,
    read_training_dataset,
)

# Test to check the savefig()
def test_make_box_diagram_path():
    submission_path = "images/Box_diagram_train.png"
    if os.path.exists(submission_path):
        os.remove(submission_path)
    make_box_diagram()
    assert os.path.exists(submission_path)
    os.remove(submission_path)
    assert submission_path is not None


# Test to check the clean_NA() function within make_diagram.py for train.csv
def test_make_box_diagram_clean_df():
    obtained_dataset = read_training_dataset()
    obtained_val_index_0_6 = obtained_dataset.iloc[0][6]
    is_nan_val_index_0_6 = np.isnan(obtained_val_index_0_6)
    assert is_nan_val_index_0_6


# Test para cehcar dimensiones de la variable axs
def test_size_subplot_axs():
    expected_size_axs = np.size(np.array([1, 2]))
    axs = make_box_diagram()
    obtained_size_axs = np.size(axs)
    assert obtained_size_axs == expected_size_axs
