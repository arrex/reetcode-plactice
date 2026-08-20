import heapq
from typing import List


class KthLargest:
    """
    Intuition:
        We use a min-heap to keep track of the k largest elements.

        Upon initialization, we heapify the input list and pop elements until
        the heap size is equal to k.

        When adding a new element, we push it onto the heap and pop the smallest
        element if the heap size exceeds k.

        When retrieving the kth largest element, we simply return the top
        element of the heap.

    Runtime:
        O(n log n) for initialization.

        O(log k) for adding an element.

        O(1) for retrieving the kth largest element.

    Memory:
        O(k) for the heap.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
