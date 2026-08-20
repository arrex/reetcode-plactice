import heapq
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        Can't use sorting, so build a max-heap. Then, we pop k-1
        elements to get the kth largest element.

    Runtime:
        Building heap takes O(n log n) since we go through all
        numbers in the array.

        Then, popping k - 1 elmts takes O((k - 1) log n).

        Overall, we have a O(n log n) runtime.

    Memory:
        Heap contains all elements before popping k - 1 elmts, so
        O(n).
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -num)

        for i in range(k - 1):
            heapq.heappop(maxHeap)

        return -maxHeap[0]


class Solution2:
    """
    Intuition:
        Instead of a max heap, we maintain a min heap of size
        k. We iterate through every elmt in nums and adjust
        our heap accordingly.

    Runtime:
        The push/pop operations take O(log k) time. We do this
        for each elmt in nums, so overall we have O(n log k).

        This runtime is better than Solution1's since we reduce
        the size of our heap from n to k.

    Memory:
        Heap bounded at size k, so O(k). This is better than
        Solution1's O(n) memory complexity.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


class Solution3:
    """
    Intuition:
        We store an array that counts the frequency of each element. The
        index represents the element and the value represents its respective
        frequency.

        We need to init the size of the array to (maxVal - minVal + 1). The +1
        is to account for the 0 value. We need at least maxVal number of slots.
        We need to also factor in the offset of minVal. This is because the
        input array can contain negative values.

        Consider if minVal is positive, then we only need maxVal - minVal + 1
        slots to hold all the numbers. If minVal is negative, then it expands
        the size of the array to account for potential negative values.

        Then, to find the kth largest number, we just iterate through the freq
        list and check the count at each index. If k drops below 0, that means
        we have found our kth largest element.

        We just need to keep in mind to offset the index where we're inserting
        at by minVal as well when building the frequency list. Also, we need
        to offset the result index.

        There exists another solution with similar runtime, but it is more
        esoteric.

    Runtime:
        O(n) to find minVal and maxVal.

        O(R) to allocate freq array where R is the range of values.

        O(n) to populate freq array.

        O(R) to iterate over the freq array to find the kth largest elmt.

        Overall runtime is O(n + R).

    Memory:
        freq array takes O(R) memory.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxVal, minVal = -inf, inf

        for num in nums:
            maxVal = max(maxVal, num)

            minVal = min(minVal, num)

        freq = [0] * int(maxVal - minVal + 1)

        for num in nums:
            freq[int(num - minVal)] += 1

        for i in range(len(freq) - 1, -1, -1):
            k -= freq[i]

            if k <= 0:
                return int(i + minVal)

        # Should never reach this point
        return -1
