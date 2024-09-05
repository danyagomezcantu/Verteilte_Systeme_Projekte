from flask import Flask, jsonify, request
from  task import *
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

    def json_to_task(self, json):
        dataset = None
        task = None
        match task:
            case 'bubble':
                self.client.tasks.append(bubble_sort(dataset))
            case 'insert':
                self.client.tasks.append(insertion_sort(dataset))
            case 'select':
                self.client.tasks.append(selection_sort(dataset))
            case 'merge':
                self.client.tasks.append(merge_sort(dataset))
            case 'quick':
                self.client.tasks.append(quick_sort(dataset))
            case 'heap':
                self.client.tasks.append(heap_sort(dataset))
            case 'count':
                self.client.tasks.append(counting_sort(dataset))
            case 'radix':
                self.client.tasks.append(radix_sort(dataset))
            case 'bucket':
                self.client.tasks.append(bucket_sort(dataset))
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
            task = self.json_to_task(task_data)
            self.client.add_task(task)
            return jsonify({'message': 'Task added'})
    def run(self):
        self.app.run(host='0.0.0.0', port=CONTAINERPORT, debug=True)
        print(f"listening on localhost:{CONTAINERPORT}")