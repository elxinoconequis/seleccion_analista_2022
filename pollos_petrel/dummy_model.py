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
    print("List files and directories: ", os.listdir())


# Limpia NA's de un DataFrame con un cero
def clean_NA(df_raw: pd.DataFrame) -> pd.DataFrame:
    check_nan_in_df = df_raw.isnull().values.any()
    if check_nan_in_df == True:
        df_clean = df_raw.fillna(0)

    elif check_nan_in_df == None:
        return df_raw

    else:
        df_clean = df_raw

    return df_clean


# Ordenar por masa
def sort_by_mass(dataset: pd.DataFrame) -> pd.DataFrame:
    df_by_mass = dataset.sort_values(by=["Masa"])
    return df_by_mass


# Ordenar por día
def sort_by_day(dataset: pd.DataFrame) -> pd.DataFrame:
    df_by_day = dataset.sort_values(by=["target"])
    return df_by_day