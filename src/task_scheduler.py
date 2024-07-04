import queue
import apscheduler as sch
from task import *
import threading as thread
from collections import deque


#TODO: what parameters can we use to schedule different tasks?
#TODO: are there any easy-to-implement schedulers to reuse?
#TODO: Can't we just "schedule" by rearranging the tasks_queue
# by different parameters like:
# -estimated time
# -priority
# -first come first serve (basically : leave as-is


thread1 =   0
thread2 =   0

queue_thread1 = queue.Queue()
queue_thread2 = queue.Queue()

tasks = queue.Queue

#TODO: Array for the performance metrics
#The metric will be stored in here
#task name
#execution time
#service time
metrics = []
def assign_thread1(task):
    queue_thread1.put(task)
def assign_thread2(task):
    queue_thread2.put(task)
def execute(tasks):
    '''
    This is the function which keeps the thread going.
    It executes all things in the queue.
    Is it filled with tasks, it executes them
    Is it filled with a None-Element, it waits for the clients to finish, terminates them and shuts down

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

def test_connection(client):
    '''
    sends a message to client to confirm a working connection
    :param client:
    :return: true/false
    '''
    return
class scheduler():
    def __init__(self, tasks, clients):
        #converts an array into a queue
        self.tasks = deque(tasks)
        self.clients = clients

    def check_clients(self):
        '''
        checks whether a client is ready for the next task or not
        :return:
        '''
        pass

    def _check_client_availability(self, client):
        '''
        Checks whether a client is ready for the next task or not.
        A client API to check is needed.
        :param client:
        :return: working or waiting
        '''
    @abstractmethod
    def start(self):
        '''
        basically the main function of the scheduler
        executes all tasks
        if no tasks are available, waits for all clients to finish
        if the clients are finished, terminates them
        :return:
        '''
        pass

    def terminate_clients(self):
        for client in self.clients:
            #send termination message via communication API
            pass
        return

class FCFS_scheduler(scheduler):
    ''''
    First Come First Serve implementation of scheduler class
    '''
    def execute(self):
        while len(self.tasks) > 0:      #checks whether tasks are left
            '''
            check availability of clients
            assert task onto clients
            
            '''
        pass