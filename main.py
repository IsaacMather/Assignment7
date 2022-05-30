import copy
import time
import random

class MinHeap:

    class EmptyHeapError(Exception):
        pass

    def __init__(self, list_in=None):
        if list_in is None:
            self._heap_list = [None]
            self._size = 0
        else:
            self._heap_list = copy.deepcopy(list_in)
            self._size = len(list_in)
            self._heap_list.insert(0, 0)
            self._order_heap()

    @property
    def size(self):
        return self._size

    def insert(self, data):
        self._heap_list.append(None)
        self._size += 1
        child_index = self._size
        while child_index > 1 and data < self._heap_list[child_index // 2]:
            self._heap_list[child_index] = self._heap_list[child_index // 2]
            child_index = child_index // 2
        self._heap_list[child_index] = data

    # def _percolate_down(self, hole):
    #     saved_off_value = self._heap_list[hole]
    #     while hole * 2 < self._size and self._heap_list[hole] > min(self._heap_list[2*hole], self._heap_list[2*hole +1]):
    #         # self._heap_list[hole] = #gotta figure out what i'm doing here,
    #         # # there's plenty of edge cases
    #         # hole = 2 * hole
    #         pass
    #
    #     self._heap_list[hole] == saved_off_value
    #
    # def find_min(self, hole):
    #
    #
    #     return min(self._heap_list[2*hole], self._heap_list[2*hole + 1])
    def _percolate_down(self, i):
        while (i * 2) <= self._size:
            mc = self.minChild(i)
            if self._heap_list[i] > self._heap_list[mc]:
                tmp = self._heap_list[i]
                self._heap_list[i] = self._heap_list[mc]
                self._heap_list[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self._size:
            return i * 2
        else:
            if self._heap_list[i * 2] < self._heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def remove(self):
        if self._size == 0:
            raise MinHeap.EmptyHeapError
        return_value = self._heap_list[1]
        self._heap_list[1] = self._heap_list[self._size]
        self._size -= 1
        self._heap_list.pop()
        if self._size > 0:
            self._percolate_down(1)
        return return_value

    def _order_heap(self):
        for i in range(self._size // 2, 0, -1):
            self._percolate_down(i)


def testing_code():

    ARRAY_SIZE = 10000

    unsorted_list = [random.randint(-10000, 10000) for _ in range(ARRAY_SIZE)]
    unsorted_list2 = copy.deepcopy(unsorted_list)

    print("MinHeap initialization and sorting ...")
    start_time = time.perf_counter()

    min_heap = MinHeap(unsorted_list)

    stop_time = time.perf_counter()

    elapsed = stop_time - start_time

    print("Initialization and Sorting ", ARRAY_SIZE, " items took", elapsed,
          "seconds")

    print("MinHeap Remove and rebalancing")
    start_time = time.perf_counter()

    unsorted_list = [min_heap.remove() for _ in range(ARRAY_SIZE)]

    stop_time = time.perf_counter()

    elapsed = stop_time - start_time

    print("Removing and re-sorting", ARRAY_SIZE, "items took", elapsed,
          "seconds")

    print()
    print("Verifying sort was correct")
    unsorted_list2.sort()

    print(f'Was the list correctly sorted? True or False? '
          f'{unsorted_list==unsorted_list2}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testing_code()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/