from sklearn import datasets
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
    obtained = clean_NA(read_training_dataset())
    assert obtained is not None


# Test para ordenar por masa del archivo train.csv
def test_sort_by_mass():
    expected_index_of_max = 185
    expected_max_mass = 104.8
    dataset = sort_by_mass(clean_NA(read_testing_dataset()))
    obtained_index = dataset["Masa"].index[-1]
    obtained_max_mass = dataset["Masa"].max()
    assert obtained_index == expected_index_of_max
    assert obtained_max_mass == expected_max_mass


# Test para ordenar por día del archivo train.csv s
def test_sort_by_day():
    expected_index_of_max = 824
    max_day = 83
    dataset = sort_by_day(clean_NA(read_training_dataset()))
    obtained_index = dataset["target"].index[-1]
    obtained_day = dataset["target"].max()
    assert obtained_index == expected_index_of_max
    assert obtained_day == max_day
