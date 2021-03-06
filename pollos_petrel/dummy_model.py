import pandas as pd
import os


# Lee train.csv
def read_training_dataset() -> pd.DataFrame:
    training_dataset_path = "pollos_petrel/train.csv"
    training_dataset = pd.read_csv(training_dataset_path)
    return training_dataset


# Calcula promedio de target
def get_target_mean(dataset: pd.DataFrame) -> float:
    mean_target = dataset["target"].mean()
    return mean_target


# Lee test.csv
def read_testing_dataset() -> pd.DataFrame:
    testing_dataset_path = "pollos_petrel/test.csv"
    testing_dataset = pd.read_csv(testing_dataset_path)
    return testing_dataset


# Tira todas las columnas excepto id
def drop_all_but_id(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset_only_id = dataset[["id"]]
    return dataset_only_id


# Agrega columna target con el promedio
def add_mean_as_target() -> pd.DataFrame:
    training_dataset = read_training_dataset()
    target_mean = get_target_mean(training_dataset)
    testing_dataset = read_testing_dataset()
    submission = drop_all_but_id(testing_dataset)
    submission["target"] = target_mean
    return submission


# Guarda el archivo con sufijo _submission.csv
def write_submission():
    submission_path = "pollos_petrel/example_python_submission.csv"
    submission = add_mean_as_target()
    submission.to_csv(submission_path)


# Imprime el actual espacio de trabajo y lista de archivos
def print_workspace():
    print("Current Working Directory: ", os.getcwd())


# Limpia NA's de un DataFrame con un cero
def clean_NA(df_raw: pd.DataFrame, fill: int) -> pd.DataFrame:
    # Is either True or False
    is_any_nan = df_raw.isnull().values.any()
    df_clean = df_raw.fillna(fill) if is_any_nan else df_raw
    return df_clean


# Ordenar por masa
def sort_by_mass(dataset: pd.DataFrame) -> pd.DataFrame:
    return dataset.sort_values(by=["Masa"])


# Ordenar por día
def sort_by_day(dataset: pd.DataFrame) -> pd.DataFrame:
    return dataset.sort_values(by=["target"])
