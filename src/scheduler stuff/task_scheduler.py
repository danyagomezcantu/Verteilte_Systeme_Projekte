import queue
import apscheduler as sch
from task import *
import threading as thread
from collections import deque
from enum import Enum


class status(Enum):
    WORKING = "working"
    WAITING = "waiting"
class scheduler():
    def __init__(self, tasks, clients):
        #converts an array into a queue
        self.tasks = deque(tasks)
        self.clients = clients
    def _test_connection(client):
        '''
        TODO: send API request to client. Look: point 3 of client __innit__()
        '''
        answer = None #
        return answer
    def _assisgn_task(self,client, task):
        '''
        TODO: send API request to client. Look: point 4 of client __innit__()
        '''
        #client.
    def check_clients(self):
        '''
        TODO: Send API request to client. Look: point 2 of client __innit__()
        checks whether a client is ready for the next task or not
        :return: a list of clients who are ready for the next task
        '''
        ready_clients = []
        for client in self.clients:
            state = None #call get_status API of client
            if state is status.WAITING:
               ready_clients.append(client)
        return ready_clients
    @abstractmethod
    def start(self):
        '''
        basically the main function of the scheduler
        executes all tasks
        if no tasks are available, waits for all clients to finish
        if the clients are finished, terminates them
        DO NOT EDIT THIS FUNCTION - THERE IS NO NEED
        '''
    def terminate_clients(self):
        '''
        TODO: send API request to client. Look: point 1 of client __innit__()
        '''
        for client in self.clients:

            #send termination message via communication API
            pass
        return

class FCFS_scheduler(scheduler):
    ''''
    First Come First Serve implementation of scheduler class
    '''
    def execute(self):
        if len(self.check_clients()) > 0:           #"clients available?"
            while len(self.tasks) > 0:              #"tasks available?"
                clients = self.check_clients()
                if clients == []:
                    continue
                for client in clients:
                    task = self.tasks.popleft()
                    self._assisgn_task(client, task)
                    pass
            print("no more tasks available. Waiting for clients to finish...")
            while (len(self.clients) != len(self.check_clients())):
                #This loop waits until all clients are done
                continue
            for client in self.clients:
                self.terminate_clients()
                pass
        else:
            print('No clients available')