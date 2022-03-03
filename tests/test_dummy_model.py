import numpy as np
from pollos_petrel import (
    add_mean_as_target,
    clean_NA,
    drop_all_but_id,
    get_target_mean,
    print_workspace,
    read_testing_dataset,
    read_training_dataset,
    sort_by_day,
    sort_by_mass,
    write_submission,
)
import os
import pandas as pd


# Lee train.csv
def test_read_training_dataset():
    training_dataset = read_training_dataset()
    obtained_n_rows = training_dataset.shape[0]
    expected_n_rows = 1304
    assert expected_n_rows == obtained_n_rows


# Calcula promedio de target
def test_get_target_mean():
    data = {"id": [1, 2], "target": [3, 4]}
    dataset = pd.DataFrame(data=data)
    obtained_mean = get_target_mean(dataset)
    expected_mean = 3.5
    assert expected_mean == obtained_mean


# Lee test.csv
def test_read_testing_dataset():
    testing_dataset = read_testing_dataset()
    obtained_n_rows = testing_dataset.shape[0]
    expected_n_rows = 326
    assert expected_n_rows == obtained_n_rows


# Tira todas las columnas excepto id
def test_drop_all_but_id():
    data = {"id": [1, 2], "target": [3, 4]}
    dataset = pd.DataFrame(data=data)
    dataset_only_id = drop_all_but_id(dataset)
    obtained_columns = list(dataset_only_id.columns)
    expected_columns = ["id"]
    assert expected_columns == obtained_columns


# Agrega columna target con el promedio
def test_add_mean_as_target():
    submission_with_mean_as_target = add_mean_as_target()
    obtained_target = submission_with_mean_as_target["target"][1]
    expected_target = 34.67101226993865
    assert expected_target == obtained_target


# Guarda el archivo con sufijo _submission.csv
def test_write_submission():
    submission_path = "pollos_petrel/example_python_submission.csv"
    if os.path.exists(submission_path):
        os.remove(submission_path)
    write_submission()
    assert os.path.exists(submission_path)
    os.remove(submission_path)
    assert submission_path is not None


# Imprime el actual espacio de trabajo y lista de archivos
def test_print_workspace(capsys):
    print_workspace()
    captured = capsys.readouterr()
    expected_string = "Current Working Directory:  /workdir"
    obtained_string = captured.out
    assert expected_string in obtained_string


# Limpia NA's de un DataFrame del archivo train.csv
def test_clean_NA_empty():
    obtained = clean_NA(read_training_dataset(), 0)
    assert obtained is not None


# Test para ordenar por masa del archivo train.csv
def test_sort_by_mass():
    expected_index_of_max_mass = 185
    dataset = sort_by_mass(clean_NA(read_testing_dataset(), 0))
    obtained_index_of_max_mass = dataset["Masa"].index[-1]
    assert obtained_index_of_max_mass == expected_index_of_max_mass
    expected_max_mass = 104.8
    obtained_max_mass = dataset["Masa"].max()
    assert expected_max_mass == obtained_max_mass


# Test para ordenar por día del archivo train.csv s
def test_sort_by_day():
    expected_index_of_max = 824
    dataset = sort_by_day(clean_NA(read_training_dataset(), 0))
    obtained_index_of_max = dataset["target"].index[-1]
    assert expected_index_of_max == obtained_index_of_max
    expected_max_day = 83
    obtained_max_day = dataset["target"].max()
    assert expected_max_day == obtained_max_day


# Function to test that the .fillna() method has the correct input, by testing trainig.csv
def test_Clean_NA_fill_NA():
    dataset = read_training_dataset()
    obtained_val_index_0_6 = dataset.iloc[0][6]
    assert np.isnan(obtained_val_index_0_6)
    clean_dataset = clean_NA(read_testing_dataset(), 0)
    obtained_val_index_0_6 = clean_dataset.iloc[0][6]
    expected_val_index_0_6 = 0
    assert obtained_val_index_0_6 == expected_val_index_0_6
