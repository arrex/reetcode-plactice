from typing import List


class Solution:
    """
    Intuition:
        Dynamic sliding window problem where we store maximum
        window size found.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0

        res = 0  # max window
        while r < len(nums):
            # ensure window is valid
            while nums[r] > nums[l] * k:
                l += 1

            # check against max window stored
            res = max(res, r - l + 1)

            r += 1

        return len(nums) - res
