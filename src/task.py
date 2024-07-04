import sorting
import time
from abc import ABC, abstractmethod

#TODO: if we were to implement scheduling strategy "round robin"
# we would have to be able to stop a tasks, save it's progress (number array)
# and readd it to the tasks queue

'''Average Time complexity table:
3:  O(n²)
2:  O(n*log(n)
1:  O(n)
'''
class task(ABC):
    def __init__(self, dataset, time_complexity):
        self.dataset = dataset
        self.time_complexity = time_complexity
        self.time = None
        self._start_time = None
        self._end_time = None
    def _taketime(self):
        self.time = self._end_time - self._start_time  # corrected time calculation
    def _start(self):
        self._start_time = time.time()
    def _end(self):
        self._end_time = time.time()
    @abstractmethod
    def _sort(self):
        pass
    def get_time_complexity(self):
        return self.time_complexity

    def sort(self):
        self._start()
        self._sort()
        self._end()
        self._taketime()
'''
Tier 3 complexities:
    -Buble sort
    -Insertion sort
    -Selection sort
'''
class bubble_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=3)  # Calls task.__init__()

    def _sort(self):
        sorting.bubble(self.dataset)

class insertion_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=3)  # Calls task.__init__()

    def _sort(self):
        arr = self.dataset
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

class selection_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=3)

    def _sort(self):
        sorting.selection(self.dataset)

'''
Tier 2 complexities:
    -merge sort
    -quick sort
    -heap sort
'''
class merge_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=2)  # Calls task.__init__()

    def _sort(self):
        sorting.merge(self.dataset)

class quick_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=2)  # Calls task.__init__()

    def _sort(self):
        sorting.quick(self.dataset)

class heap_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=2)  # Calls task.__init__()

    def _sort(self):
        sorting.heap(self.dataset)  # assuming there is a heap sort function in sorting module

'''
Tier 1 complexities:
    -counting sort
    -radix sort
    -bucket sort
'''

class counting_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset,time_complexity=1)

    def _sort(self):
        pass
class radix_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=1)
    def _sort(self):
        sorting.counting(self.dataset)
class bucket_sort(task):
    def __init__(self, dataset):
        super().__init__(dataset, time_complexity=1)
    def _sort(self):
        sorting.bucket(self.dataset)