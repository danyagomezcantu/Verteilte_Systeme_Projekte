from task import *
from collections import deque
from enum import Enum
import requests
import docker
'''
TODO: save host- and container ports per client
'''

'''
The service was defined on Port 5000.
This is not good practice but I (supposedly) need the container port to map onto the hostpath'''
CONTAINER_PORT = '5000/tcp'

docker = docker.from_env()
def _get_host_port(id):
    """
       Funktion zum Abrufen des Host-Ports, der mit einem bestimmten Container-Port verbunden ist.
       :param container: Docker-Container-Objekt
       :param container_port: Der Port im Container (z.B. '5000/tcp')
       :return: Der zugewiesene Host-Port als String oder None, wenn nicht vorhanden
       """
    container = docker.containers.get(id)
    ports = container.attrs['NetworkSettings']['Ports']
    port_info = ports.get(CONTAINER_PORT)
    if port_info and port_info[0]:
        return port_info[0]['HostPort']
    print("Error! could not retrieve Hostport")
    return None
def _get_client_ip(id):
    hostport = _get_host_port(id)
    return f"http://localhost:{hostport}"
class status(Enum):
    WORKING = "working"
    WAITING = "waiting"
class scheduler(ABC):
    def __init__(self, tasks, clients):
        #converts an array into a queue
        self.tasks = deque(tasks)
        self.client_ids = clients

    def _test_connection(self, client):
        '''
        Optional for debugging
        '''
        answer = None #
        return answer
    def assign_task(self, client, task):
        '''
        TODO: send API request to client. Look: point 4 of client __innit__()
        PROBLEM: The API is not capable of receiving task objects
        Solution: Let the API itself create a task in the container
        send dataset to client
        '''
    @abstractmethod
    def execute(self):
        pass
    def check_clients(self):
        '''
        TODO: Send API request to client. Look: point 2 of client __innit__()
        checks whether a client is ready for the next task or not
        :return: a list of clients who are ready for the next task
        need:
        - HOST-port
        -ip (localhost)
        -url-path
        '''
        ready_clients = []
        for client in self.client_ids:
            client_ip = _get_client_ip(client)
            url = f"{client_ip}/status"
            print(f"Sending status request to {url}")
            state = requests.get(url)
            if state is status.WAITING:
               ready_clients.append(client)
        return ready_clients
    def terminate_clients(self):
        '''
        TODO: send API request to client. Look: point 1 of client __innit__()
        '''
        for client in self.client_ids:

            #send termination message via communication API
            pass
        return

class FCFS_scheduler(scheduler):
    ''''
    First Come First Serve implementation of scheduler class
    '''
    def execute(self):
        '''
        The FCFS scheduler checks whether tasks are left to assign,
        then what clients are available and assigns them.
        When all tasks are assigned the scheduler waits for the clients to finish theirs
        and shuts them down when they are.
        Whether the client is available is defined by
        TODO: definie clients availability
        '''
        while len(self.tasks) > 0:
            clients = self.check_clients()
            if clients == []:
                continue
            for client in clients:
                task = self.tasks.popleft()
                self.assign_task(client, task)
                pass
        print("no more tasks available. Waiting for clients to finish...")
        while (len(self.client_ids) != len(self.check_clients())):
            #This loop waits until all clients are done
            continue
        for client in self.client_ids:
            self.terminate_clients()
            pass
        '''
        TODO (optional): Implement safety measures to assure that clients have successfully shut down.'''