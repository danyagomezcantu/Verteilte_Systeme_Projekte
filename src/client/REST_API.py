from flask import Flask, jsonify, request
#from src/scheduler stuff import task.py
'''
Because the client runs an infinite loop I decided to make the API an external object which acts as it's own.
The client owns the API as an object attribute. The API receives the Client as an argument to access the clients values.
PROBLEM:
I cannot send Python Objects via Flask to the Client via the API.
Solutions:
1. let the taks get created on the client side. The main-skripts sends a json with the necessary information.
'''
HOSTPORT = 5000

class API:
    def __init__(self, client):
        self.app = Flask(__name__)
        self.client = client
        self.setup_routes()

    def create_task_from_data(self, data):
        # TODO: Implement this function to convert received JSON data to a task object
        pass
    def setup_routes(self):
        @self.app.route('/status', methods=['GET'])
        def status():
            return jsonify({'status': self.client.get_status().value})

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
        '''
        TODO: We need a way to find out the hostport on which this docker container runs on.
        The script itself has no idea in which container it is running and therefore has no information about it.
        There might be the option to set ENV variables during the creation of the container (in the dockerfile itself).
        But because the host port is generated randomly there seems to be no option to set ENV variables.
        Creating 2 disctinct containers with static ports would make the project less maintainable.
        '''
        self.app.run(host='0.0.0.0', port=HOSTPORT)
