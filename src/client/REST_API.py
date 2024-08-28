from flask import Flask, jsonify, request
#from src/scheduler import task.py
'''
Because the client runs an infinite loop I decided to make the API an external object which acts as it's own.
The client owns the API as an object attribute. The API receives the Client as an argument to access the clients values.
PROBLEM:
I cannot send Python Objects via Flask to the Client via the API.
Solutions:
1. let the taks get created on the client side. The main-skripts sends a json with the necessary information.
'''
CONTAINERPORT = 5000

class API:
    def __init__(self, client):
        self.app = Flask(__name__)
        self.client = client
        self.setup_routes()

    def create_task_from_data(self, data):
        # TODO: Implement this function to convert received JSON data to a task object
        # we need to import task.py
        # case switch
        pass
    def setup_routes(self):
        #TODO: NO GUARANTEE these paths work - generated with ChatGPT
        # 1. Get Status (working or waiting?)
        # 2. terminate() --> close container
        # 3.
        @self.app.route('/status', methods=['GET'])
        def status():
            return jsonify({'status': self.client.get_status()})

        @self.app.route('/terminate', methods=['POST'])
        def terminate():
            self.client.terminate()
            return jsonify({'message': 'Client terminated'})

        @self.app.route('/add_task', methods=['POST'])
        def add_task():
            task_data = request.get_json()
            # You need to implement a way to create a task from task_data
            task = self.create_task_from_data(task_data)
            self.client.add_task(task)
            return jsonify({'message': 'Task added'})
    def run(self):
        self.app.run(host='0.0.0.0', port=CONTAINERPORT, debug=True)
        print(f"listening on localhost:{CONTAINERPORT}")