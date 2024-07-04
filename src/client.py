import queue
from enum import Enum
'''
The Idea for client.py is that it is implemented on the Docker containers to:
1. wait for tasks
2. execute tasks
3. update execution status & return execution metrics

'''
class status(Enum):
    WORKING = "working"
    WAITING = "waiting"

class client():
    def __init__(self):
        self.comm = None #Communication Interface for task submission, status query or client termination
        self.status = status.WAITING
        self.tasks = queue.Queue
        pass

    def _tasks_available(self):
        if len(self.tasks) > 0:
            return True
        else:
            return False
    def get_status(self):
        return self.status

    def execute(self):
        self.status = status.WORKING
        pass

'''
I am currently not sure on how to communicate between scheduler and clients.
First of all: 
The scheduler must know if the client is working or not.
Does the scheduler check the clients status or does the client report to the scheduler?

Second:
How do I guarantee the clients status report is getting received?
Either the scheduler or the client has to listen to a communication channel to incoming requests.
I tend to prefer the scheduler to check the clients status since it's his job to distribute the workload.
Based on this preference I have to guarantee that the client leaves a communication channel always open
to be checked on the working status.
'''