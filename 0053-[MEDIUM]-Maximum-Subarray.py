from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        We maintain a dynamic sliding window. We increment the right ptr
        as long as our sum is increasing. Whenever our sum dips below
        0, we adjust our left ptr and the current sum of the window
        accordingly.

    Runtime:
        O(n). Linear sliding window solution.

    Memory:
        O(1).
    """

    def maxSubArray(self, nums: List[int]) -> int:
        curr, res = 0, -inf
        l, r = 0, 0

        while r < len(nums):
            while curr < 0:
                curr -= nums[l]
                l += 1

            curr += nums[r]

            res = max(res, curr)

            r += 1

        return res


class Solution2:
    """
    Intuition:
        We can use the idea of a sliding window, but optimize it. Notice
        that we don't need to maintain a left ptr because we just reset
        the current sum to 0 whenever it becomes negative. Thus, we
        simplify our loop a lot.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        curr = 0

        for n in nums:
            curr = max(curr, 0)
            curr += n
            res = max(res, curr)

        return res


class Solution3:
    """
    Intuition:
        Kandane's algorithm with DP approach. Same idea of tracking current sum
        and highest sum, except the current sum can just be set to the current
        element in the array as a "reset".

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            res = max(res, curr)

        return res
