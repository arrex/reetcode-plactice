from typing import List


class Solution:
    """
    Intuition:
        The problem is essentially just asking us to return a non-decreasing
        array in disguise. To do this, we keep track of the largest value
        encountered.
    """

    def maximumPossibleSize(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = []

        for num in nums:
            if not res or num >= res[-1]:
                res.append(num)

        return len(res)
