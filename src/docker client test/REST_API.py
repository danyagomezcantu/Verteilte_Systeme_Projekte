from flask import Flask, jsonify, request
'''
Because the client runs an infinite loop I decided to make the API an external object which acts as it's own.
The client owns the API as an object attribute. The API receives the Client as an argument to access the clients values.
PROBLEM:
I cannot send Python Objects via Flask to the Client via the API.
Solutions:
1. let the taks get created on the client side. The main-skripts sends a json with the necessary information.
'''

class API():
    def __init__(self, client):
        self.client = client
        self.app = Flask(__name__)

    @app.route('/status',methods=['GET'])
    def status(self):
        self.client.get_status()

    @app.route('/terminate', methods=['POST'])
    def terminate(self):
        self.client.terminate()

    @app.route('/add_task', methods=['POST'])
    def add_task(self):
        '''
           TODO: READ incoming JSON-files and convert them back into task-objects.
            Maybe through importing the task.py into the clients too.
        '''
        self.client.add_task()
