from typing import List


class Solution:
    """
    Intuition:
        Use dynamic sliding window approach.

        One pass to find longest strictly increasing subarray and a second
        pass to find longest strictly decreasing subarray.

    Runtime:
        O(2 * n) ~ O(n) for the 2 linear passes.

    Memory:
        O(1).
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        # find longest strictly increasing window
        curr, longestIncr = 1, 1
        for r in range(1, N):
            if nums[r] > nums[r - 1]:
                curr += 1
            else:
                curr = 1

            if curr > longestIncr:
                longestIncr = curr

        # find longest strictly decreasing window
        curr, longestDecr = 1, 1
        for r in range(1, N):
            if nums[r] < nums[r - 1]:
                curr += 1
            else:
                curr = 1

            if curr > longestDecr:
                longestDecr = curr

        return max(longestIncr, longestDecr)
