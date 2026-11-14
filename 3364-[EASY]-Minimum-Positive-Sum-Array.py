from math import inf
from typing import List


class Solution:
    """
    Intuition:
        Use a fixed sliding window size while cycling through all valid
        subarray sizes.

    Runtime:
        Each sliding window run takes O(n) time. We have (r - l + 1)
        different sizes to go through, so total runtime is O(n * (r - l + 1)).

    Memory:
        O(1).
    """

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        N = len(nums)
        res = inf

        for size in range(l, r + 1):
            curr = sum(nums[0:size])

            if curr > 0 and curr < res:
                res = curr

            for right in range(size, N):
                curr -= nums[right - size]
                curr += nums[right]

                if curr > 0 and curr < res:
                    res = curr

        return res if res != inf else -1
