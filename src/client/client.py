import queue
from enum import Enum
import threading
from REST_API import API
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
        yes:
        -container_object.kill()
        -.stop()
        If there is a way to destroy a docker container this might be the function for it
        '''
        self.terminated = 1
    def get_status(self):
        return self.status.value
    def start(self):
        print("test")
        ''' TODO: I think the connect the API needs to be started here'''
        #TODO: Do we make adding tasks dependend on the state or the queue itself?
        self.status = status.WAITING
        while not self.terminated:
            if self._tasks_available():
                task = self.tasks.get()
                task.sort()
            else:
                #With the state I can make sure when no more tasks are available
                #the client does not get interrupted while working
                self.status = status.WAITING

if __name__ == '__main__':
    client = client()
    api = API(client)
    print("testprint: Is this script even being executed in the container?")
    client_thread = threading.Thread(target=client.start)
    client_thread.start()
    api.run()