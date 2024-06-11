import time
class task:
    def __init__(self, dataset):
        self.dataset = dataset
        self.time
        self._start_time
        self._end_time

    def _taketime(self):
        self.time = self._start_time - self._end_time
    def _start(self):
        self._start_time = time.time()
    def _end(self):
        self._end_time = time.time()

class bubblesort(task):

    def sort(self):
        self._start()
        #do-something
        self._end()
        self._taketime()
        pass