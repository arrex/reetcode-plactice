import heapq
from math import sqrt
from typing import List


class Solution:
    """
    Intuition:
        Use a max heap to track distances. Since we have
        a max heap, the point with the highest distance
        will be at the root. Thus, if we need to evict,
        we can simply just pop the root.

    Runtime:
        Each point processed once, push/pop operations take
        O(log k) time. Overall O(n log k) time.

        Since k < n, it would be more advantageous if we can
        apply the log factor on n instead of k. O(k log n)
        runtime is possible with a min-heap.

    Memory:
        O(k) for the heap.
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = -sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, (dist, [x, y]))

            # need to evict
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [p for _, p in maxHeap]
