import sorting
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
        sorting.bubble(self.dataset)
        self._end()
        self._taketime()
        pass

class insertion_sort(task):
    def sort(self):
        self._start()
        self._insertion_sort(self.dataset)
        self._end()
        self._taketime()
        pass

    def _insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

class merge_sort(task):
    def sort(self):
        self._start()
        sorting.merge(self.dataset)
        self._end()
        self._taketime()
        pass


class quick_sort(task):
    def sort(self):
        self._start()
        sorting.quick(self.dataset)
        self._end()
        self._taketime()
        pass

class heap_sort(task):
    def sort(self):
        self._start()
        # do-something
        self._end()
        self._taketime()
        pass


def main():
    print("what kind of scheduler do you want to use?")
    print("Option 1:    First Come First Serve")
    print("Option 2:    Shortest Job First")
    print("Option 3:    ")