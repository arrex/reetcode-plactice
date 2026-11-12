from typing import List


class Solution1:
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


class Solution2:
    """
    Intuition:
        Same as Solution1. We merge both linear passes into a single
        pass instead.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        currIncr, longestIncr = 1, 1
        currDecr, longestDecr = 1, 1
        for r in range(1, N):
            # adjust strictly increasing window
            if nums[r] > nums[r - 1]:
                currIncr += 1
            else:
                currIncr = 1

            if currIncr > longestIncr:
                longestIncr = currIncr

            # adjust strictly decreasing window
            if nums[r] < nums[r - 1]:
                currDecr += 1
            else:
                currDecr = 1

            if currDecr > longestDecr:
                longestDecr = currDecr

        return max(longestIncr, longestDecr)
