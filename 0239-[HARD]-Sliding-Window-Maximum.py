import heapq
from collections import deque
from typing import List


class Solution1:
    """
    Intuition:
        We use a max heap to keep track of the greatest element in the current window.
        We store tuples that contain the value as well as its index within our heap.
        Whenever we update out window, we check the root of our max heap to see if it
        is still valid. If the index is less than the left index (r - k + 1), then we
        pop it. Continue this process until our new max is valid (i.e. it falls within
        the current window).

    Runtime:
        Each element in the input array is processed once which gives us O(n). For each
        element, it is pushed onto the heap at most once and popped from it at most once
        as well. Pushing onto the heap takes O(log k) time since the heap has size k.
        Popping from the heap also takes O(log k) time. Therefore, the overall time
        complexity is O(n * log k). Since k = n in the worst case, then our new overall
        complexity becomes O(n * log n)

    Memory:
        We need to store a heap of size k which brings our overall memory complexity to
        O(k). Once again, since k = n in the worst case, we have O(n) as our new overall
        space complexity.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        maxH = []
        for ix in range(k):
            n = nums[ix]
            heapq.heappush(maxH, (-n, ix))

        currMax, _ = maxH[0]
        res = [-currMax]

        for r in range(k, len(nums)):
            _, peekIx = maxH[0]
            while peekIx < r - k + 1:
                heapq.heappop(maxH)

                if not maxH:
                    break

                _, peekIx = maxH[0]

            heapq.heappush(maxH, (-nums[r], r))

            root, ix = maxH[0]
            res.append(-root)

        return res


class Solution2:
    """
    Intuition:
        Same as Solution1. Just rewritten in a much more elegant way.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                res.append(-heap[0][0])

        return res


class Solution3:
    """
    Intuition:
        Instead of using a heap to track the elements in our current window, we model the same
        idea using the double-ended deque data structure. This queue will always be in decreasing
        order with the current max at index 0.

        Why do we model our deque like so? Because if I encounter a max element inside a window,
        I don't care about any element preceding it, and therefore can remove them.

        As an added step, we also need to keep track if the current max goes out of scope as we
        increment our window and delete it accordingly.

    Runtime:
        Each elmt of nums is processed once, leading to O(n). Each elmt is added to the queue and
        popped from the queue at most once as well. Popping and appending to the queue takes O(1)
        time. Therefore, the overall time complexity is O(n).

    Memory:
        The queue we store contains at most n elements where n is the length of nums. Thus, the
        memory complexity is O(n).
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()

            q.append(nums[i])

        res.append(q[0])

        for i in range(k, len(nums)):
            # remove elmt falling out of window if it's the current max
            if q and q[0] == nums[i - k]:
                q.popleft()

            while q and q[-1] < nums[i]:
                q.pop()

            q.append(nums[i])
            res.append(q[0])

        return res
