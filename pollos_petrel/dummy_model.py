import pandas as pd
import os
import matplotlib

# Lee train.csv
def read_training_dataset() -> pd.DataFrame:
    #id,Masa,Longitud_tarso,Longitud_ala,Longitud_pico,Longitud_pluma_interior_de_la_cola,Longitud_pluma_exterior_de_la_cola,target
    #[],[],[],[],[]
    # path to /pollos_petrel
    #C:\Users\Fernando\Desktop\GECI-Seleccion_analista\seleccion_analista_2022_JFOS\pollos_petrel
    submission_file_name = "JFOS_submission.csv"
    training_dataset_path = "C:/Users/Fernando/Desktop/GECI-Seleccion_analista/seleccion_analista_2022_JFOS/pollos_petrel/train.csv"
    training_dataset = pd.read_csv(training_dataset_path)
    print(type(training_dataset))

    return training_dataset


# Calcula promedio de target
def get_target_mean(dataset: pd.DataFrame) -> float:
    mean_target = dataset["target"].mean()
    return mean_target


# Lee test.csv
def read_testing_dataset() -> pd.DataFrame:
    testing_dataset_path = "C:/Users/Fernando/Desktop/GECI-Seleccion_analista/seleccion_analista_2022_JFOS/pollos_petrel/test.csv"
    testing_dataset = pd.read_csv(testing_dataset_path)
    print(type(testing_dataset))
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


## ------MAIN-----------------------
cwd=os.getcwd()
print("\nCurrent Working Directory",cwd)
print("List files and directories: ", os.listdir())
print("Pandas version: ", pd.__version__)


print("Leer /train.csv")
x=read_training_dataset()
print("Leer test.csv")
y=read_testing_dataset()

