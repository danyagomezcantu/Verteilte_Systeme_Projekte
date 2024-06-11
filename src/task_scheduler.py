import apscheduler as sch
import sorting
import numpy as np
import pandas as pd


def create_dataset(start=1, end=101, size=200):
    print("generating "+str(size)+" numbers between "+str(start)+" and "+str(size))

    array = np.random.randint(start, end, size)
    df = pd.DataFrame(array)
    df.to_csv("dataset.csv", index=False)

def dataset_to_array(dataset):
    dataframe = pd.read_csv(dataset)
    return dataframe.to_numpy()

