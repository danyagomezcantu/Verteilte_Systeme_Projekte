import time

from flask import Flask
from src.client.REST_API import API
import docker
import requests

dock = docker.from_env()
apiclient = docker.APIClient()

CONTAINER_PORT = "5000/tcp"
def create_client(dock):
    try:
        container = dock.containers.run(
            image="vs_client",  #the name of the image I created in the dockerfile
            detach=True,
            ports={'5000/tcp': None}) #Container-port is 5000 Host-port is generated randomly
    except:
        print("Container failed to run")
    return container.id

def _get_host_port(id):
    """
       Funktion zum Abrufen des Host-Ports, der mit einem bestimmten Container-Port verbunden ist.
       :param container: Docker-Container-Objekt
       :param container_port: Der Port im Container (z.B. '5000/tcp')
       :return: Der zugewiesene Host-Port als String oder None, wenn nicht vorhanden
       """
    container = dock.containers.get(id)
    ports = container.attrs['NetworkSettings']['Ports']
    print(ports)
    port_info = ports.get(CONTAINER_PORT)
    if port_info and port_info[0]:
        return port_info[0]['HostPort']
    print("Error! could not retrieve Hostport")
    return None
    # result = apiclient.port(id, CONTAINER_PORT)
    # print(result)
def _get_client_ip(id):
    hostport = _get_host_port(id)
    print(f"hostport:{hostport}")
    return f"http://localhost:{hostport}"



if __name__ == '__main__':
    client = create_client(dock)
    time.sleep(5)
    print(f"client ID:{client}")
    client_ip = _get_client_ip(client)
    url = f"{client_ip}/status"
    print(f"Sending status request to {url}")
    state = requests.get(url)
    print(state)
