import math
from typing import List


class Solution:
    """
    Intuition:
        Given that the threshold is always greater than or equal to the
        number of piles, we can derive that the upper bound for the
        consumption rate `k` is the maximum value in the piles array
        (eat one pile per hour). Let us denote the maximum value in the
        piles array as 'm'.

        A brute force approach would involve checking each k between 1 and
        'm'. However, we can be smarter and use a binary search approach.

    Runtime:
        O(n log m) where n is the number of elements in piles and m is
        the maximum value encountered in the pile.

    Memory:
        O(1) since we only store pointers.
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)

            if time <= h:
                r = k - 1
            else:
                l = k + 1

        return l
