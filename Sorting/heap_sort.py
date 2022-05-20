from helpers import get_test_case, swap


class Heap:
    def __init__(self, array: list[int]) -> None:
        self.list = array
        self.heap = []

    def get_parent(self, index: int):
        return index // 2

    def get_children(self, index: int):
        return [2 * index, 2 * index + 1]

    def bubble_up(self, index: int):
        if index == 0:
            return

        parent_index = self.get_parent(index)

        if parent_index == index:
            return

        if self.heap[parent_index] > self.heap[index]:
            swap(self.heap, index, parent_index)

        self.bubble_up(parent_index)

    def bubble_down(self, index: int = 0):
        if index >= len(self.heap):
            return

        left, right = self.get_children(index)

        to_swap_with = left

        if left > len(self.heap) - 1:
            return

        if right < len(self.heap) and self.heap[right] < self.heap[left]:
            to_swap_with = right

        if self.heap[to_swap_with] >= self.heap[index]:
            return

        swap(self.heap, to_swap_with, index)

        self.bubble_down(to_swap_with)

    def get_min_element(self):
        swap(self.heap, 0, len(self.heap) - 1)

        to_return = self.heap.pop()

        self.bubble_down(0)

        return to_return

    def heap_sort(self):
        sorted_array = []

        while len(h.heap) > 0:
            sorted_array.append(self.get_min_element())

        return sorted_array

    def heapify(self):
        for index, element in enumerate(self.list):
            self.heap.append(element)
            self.bubble_up(index)


for case in get_test_case(30):
    h = Heap(case)
    h.heapify()

    print(sorted(case[:]) == h.heap_sort())
