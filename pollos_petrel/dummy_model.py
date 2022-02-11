import pandas as pd
import os
import matplotlib

# Lee train.csv
def read_training_dataset() -> pd.DataFrame:
    submission_file_name = "JFOS_submission.csv"
    training_dataset_path = "pollos_petrel/train.csv"
    training_dataset = pd.read_csv(training_dataset_path)
    print("Length: ",len(training_dataset),type(training_dataset))
    print(training_dataset.head())

    return training_dataset


# Calcula promedio de target
def get_target_mean(dataset: pd.DataFrame) -> float:
    mean_target = dataset["target"].mean()
    return mean_target


# Lee test.csv
def read_testing_dataset() -> pd.DataFrame:
    testing_dataset_path = "pollos_petrel/test.csv"
    testing_dataset = pd.read_csv(testing_dataset_path)
    print("Length: ",len(testing_dataset),type(testing_dataset))
    print(testing_dataset.head())
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
def write_submission(dataset: pd.DataFrame,filename=""):
    submission_path = "pollos_petrel/"+filename
    submission = add_mean_as_target()
    submission.to_csv(submission_path)


## ------MAIN-----------------------
cwd=os.getcwd()
print("\nCurrent Working Directory",cwd)
print("List files and directories: \n", os.listdir())
print("Pandas version: ", pd.__version__)


# 1.- Ajusta un modelo con el archivo train.csv
print("\nLeer /train.csv")
df_train=read_training_dataset()

df.train=df_train.fillna(0)
print(df_train[["Masa","target"]])

sort_by_mass = df_train.sort_values(by=["Masa"])
print(sort_by_mass)

sort_by_day=df_train.sort_values(by=["target"])
print(sort_by_day)

# 2.- Evalúa el modelo ajustado en test.csv
#print("\nLeer /test.csv")
#df_test=read_testing_dataset()


# 3.- Guarda la respuesta en un archivo .csv
submission_file_name = "JFOS_submission.csv"

# Resultado: Estimar la edad de acuerdo a la morfometría
# id,edad estimada

