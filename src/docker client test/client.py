import docker
import queue
from enum import Enum
from flask import Flask, jsonify, request
'''
The Idea for client.py is that it is implemented on the Docker containers to:
1. wait for tasks
2. execute tasks
3. update execution status & return execution metrics
It's basically the main function for the docker container
'''
class status(Enum):
    WORKING = "working"
    WAITING = "waiting"

class client():
    def __init__(self):
        self.comm = None #Communication Interface for task submission, status query or client termination
        '''
        The communication should feature a port/command for:
        1. Termination of the container via _terminate()
        2. Status request via get_status()
        3. connection testing via _isconnected()
        4. receive task via _add_task()
        '''
        self.status = status.WAITING
        self.tasks = queue.Queue()
        self.terminated = 0        #terminated is the variable which ends the loop and therefore terminates the client
        self.start()
    def add_task(self, task):
        self.tasks.put(task)
    def _isconnected(self):
        '''
        If the message is being received it returns True.
        :return:
        '''
        return True
    def _tasks_available(self):
        if self.tasks.empty():
            return False
        else:
            True
    def terminate(self):
        '''
        TODO: Is there a way to terminate/stop docker containers?
        If there is a way to destroy a docker container this might be the function for it
        '''
        self.terminated = 1
    def get_status(self):
        return self.status
    def start(self):
        print("test")
        '''TODO: I think the connect the API needs to be started here'''
        self.status = status.WORKING
        while not self.terminated:
            if self._tasks_available():
                task = self.tasks.get()
                task.sort()
            else:
                self.status = status.WAITING

class API():
    def __init__(self, client):
        self.app = Flask(__name__)
        self.client = client
    @app.route('/status',methods=['GET'])
    def status(self):
        self.client.get_status()

    @app.route('/terminate', methods=['POST'])
    def terminate(self):
        self.client.terminate()

    @app.route('/add_task', methods=['POST'])
    def add_task(self):
        self.client.add_task()


client = client()
api = API(client)
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

if __name__ == '__main__':
    client.start()