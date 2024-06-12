import queue

import apscheduler as sch
import sorting
import numpy as np
import pandas as pd
import threading as thread

thread1 =   0
thread2 =   0

queue_thread1 = queue.Queue()
queue_thread2 = queue.Queue()
def assign_thread1(task):
    queue_thread1.put(task)

def assign_thread2(task):
    queue_thread2.put(task)

def create_queue():
    '''
    Wir müssen eine Queue an Tasks erstellen, deren Elemente an die Threads übergeben werden.
    Wird ein Element übergeben, wird es aus der Queue entfernt.
    Gibt es keine Elemente in der Queue und die Threads haben ihre Aufgaben erfüllt,
    dann soll das Hauptprogrmam beendet werden
    :return:
    '''
def create_dataset(start=1, end=101, size=200):
    print("generating "+str(size)+" numbers between "+str(start)+" and "+str(size))

    array = np.random.randint(start, end, size)
    df = pd.DataFrame(array)
    df.to_csv("dataset.csv", index=False)


def dataset_to_array(dataset):
    dataframe = pd.read_csv(dataset)
    return dataframe.to_numpy()

def execute(tasks):
    '''
    This is the function which keeps the thread going.
    It executes all things in the queue.
    Is it filled with tasks, it executes them
    Is it filled with a None-Element, then it shuts down

    :param tasks: A queue full of instances of the class task
    :return:
    '''
    working = 0
    while True:
        try:
            task = tasks.get_nowait()
        except queue.Empty:
            continue

        if task is None:
            print("Queue is None - ending Thread!")
            break
        working = 1
        task.sort()
        working = 0

