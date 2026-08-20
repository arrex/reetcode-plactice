from typing import List


class Solution:
    """
    Intuition:
        Use a fixed sliding window of size k. We are given in the
        constraints that there are at least k elements in the input
        array, so we start the current sum of the first k elements.

        We track sums instead of averages since the max average is a
        reflection of the max sum. At each iteration, we modify the
        current sum by subtracting the leftmost element and adding the
        rightmost element (new number).

    Runtime: O(n)

    Memory: O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum -= nums[i - k]
            currSum += nums[i]

            maxSum = max(maxSum, currSum)

        return maxSum / k
