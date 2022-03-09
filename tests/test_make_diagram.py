import numpy as np
import os
from pollos_petrel import make_box_diagram, clean_NA, read_training_dataset


# Test to check the savefig()
def test_make_box_diagram_path():
    submission_path = "images/Box_diagram_train.png"
    if os.path.exists(submission_path):
        os.remove(submission_path)
    make_box_diagram(clean_NA(read_training_dataset(), 0))
    assert os.path.exists(submission_path)
    os.remove(submission_path)
    assert submission_path is not None


# Test to check the clean_NA() function within make_diagram.py for train.csv - revisar
def test_make_box_diagram_clean_df():
    obtained_dataset = read_training_dataset()
    obtained_val_index_0_6 = obtained_dataset.iloc[0][6]
    is_nan_val_index_0_6 = np.isnan(obtained_val_index_0_6)
    assert is_nan_val_index_0_6


# Test para checar dimensiones de la variable axs, para train.csv
def test_size_subplot_axs():
    expected_size_axs = np.size(np.array([1, 2]))
    axs = make_box_diagram(clean_NA(read_training_dataset(), 0))
    obtained_size_axs = np.size(axs)
    assert obtained_size_axs == expected_size_axs


# Test para el primer subplot
def test_plot_first_subplot():
    clean_df = clean_NA(read_training_dataset(), 0)
    obtained_axs = make_box_diagram(clean_df)  # from matplotlib
    obtained_axs_name = obtained_axs[0].get_title(loc="center")
    expected_axs_name = "Días"
    assert obtained_axs_name == expected_axs_name


# Test para el segundo subplot
def test_plot_second_subplot():
    clean_df = clean_NA(read_training_dataset(), 0)
    obtained_axs = make_box_diagram(clean_df)  # from matplotlib
    obtained_axs_name = obtained_axs[1].get_title(loc="center")
    expected_axs_name = "Masa"
    assert obtained_axs_name == expected_axs_name
