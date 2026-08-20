from collections import defaultdict
from typing import List


class Solution:
    """
    Intuition:
        Compute what the frequency counter should look like.

        Then compute what it actually is and compare expected
        vs actual.

    Runtime:
        O(n) since we have 2 linear passes.

    Memory:
        O(n) space for the 'good' and 'counter' dictionaries.
    """

    def isGood(self, nums: List[int]) -> bool:
        N = len(nums)
        good = {i: 1 for i in range(1, N - 1)}
        good[N - 1] = 2

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        return counter == good
