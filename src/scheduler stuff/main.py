import numpy as np
import pandas as pd
from task import *
from task_scheduler import *
import docker

'''
The main will be executed on the comuter itself.
    1. generate or select dataset
    2. generate tasks
    3. select scheduler
    4. connect clients
    5. start tasks execution via scheduler
    6. terminate clients and end main
'''
def select_scheduler(tasks, clients):
    print("Finally what kind of scheduler do you want to use?")
    print("Option 1:    First Come First Serve")
    print("Option 2:    Shortest Job First")
    print("Option 3:    Round Robin")
    option = input()
    #TODO: remove other options - we focus only on FCFS
    match option:
        case "1":
            #create FCFS scheduler
            return FCFS_scheduler(tasks,clients)
        case "2":
            #create SJF scheduler
            return
        case "3":
            #create round robin scheduler
            return
        case default:
            print("wrong input please try again")
            select_scheduler()

def select_tasks(dataset):
    print("Now which tasks do you want to schedule?")
    print("Here are the options by time complexity (1:fastest, 2:medium, 3:slow):")
    print("Tier 1:\n11:\tbubble sort\n12:\tinsertion sort\n13:\tselection sort\n")
    print("Tier 2:\n21:\tmerge sort\n22:\tquick sort\n23:\theap sort\n")
    print("Tier 3:\n31:\tcounting sort\n32:\tradix sort\n33:\tbucket sort\n")
    print("0 to complete task selection")
    tasks = []
    option = None

    while option != "0":
        option = input()
        match option:
            #Tier 1
            case "11":  tasks.append(bubble_sort(dataset))
            case "12":  tasks.append(insertion_sort(dataset))
            case "13":  tasks.append(selection_sort(dataset))
            #Tier 2
            case "21":  tasks.append(merge_sort(dataset))
            case "22":  tasks.append(quick_sort(dataset))
            case "23":  tasks.append(heap_sort(dataset))
            #Tier 3
            case "31":  tasks.append(counting_sort(dataset))
            case "32":  tasks.append(radix_sort(dataset))
            case "33":  tasks.append(bucket_sort(dataset))
            case "0":   pass
            case default:
                print("wrong option please try again")
    return tasks

def gen_dataset():
    #TODO: input security
    print("First you want to generate a dataset of numbers to sort")
    print("Do you want to create a new dataset or use an existing one?\n1: yes\n0: no")
    option = int(input())
    while option != "1" and option != "0":
        print("wrong option please try again")
    if option == "1":
        return _dataset_to_array()
    print("Enter the beginning, then the end of number range to generate from")
    start = int(input())
    end = int(input())
    print("Now enter the total size of the dataset")
    size = int(input())
    print("generating " + str(size) + " numbers between " + str(start) + " and " + str(size)+"\n")
    array = np.random.randint(start, end, size)
    return array

def _create_dataset(start=1, end=101, size=200):
    array = np.random.randint(start, end, size)
    return array
def _dataset_to_csv(array):
    df = pd.DataFrame(array)
    df.to_csv("dataset.csv", index=False)
def _dataset_to_array(dataset = "dataset.csv"):
    dataframe = pd.read_csv(dataset)
    return dataframe.to_numpy()
def create_client(dock):
    try:
        container = dock.containers.run(
            image="vs_client",  #the name of the image I created in the dockerfile
            detach=True,
            ports={5000: None}) #Container-port is 5000 Host-port is generated randomly
    except:
        print("Container failed to run")
    '''
        TODO: The Container ID's don't match those shown in docker Desktop!!!!
        This is the root cause that NO API WORKS right now.
        Without the right ID we're not able to retrieve the necessary information'''
    return container.id

if __name__ == "__main__":
    dock = docker.from_env()
    dataset = _dataset_to_array()
    tasks = select_tasks(dataset)
    client1 = create_client(dock)
    client2 = create_client(dock)
    scheduler = select_scheduler(tasks, [client1, client2])
    scheduler.execute()