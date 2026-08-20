from typing import List


class Solution:
    """
    Intuition:
        Maintain 2 pointers. Start at both extremes of input array
        and slowly make way towards center. We modify pointers in a
        "greegy" manner as in we modify whichever one has a lower
        height in the hopes of maximizing volume.

    Runtime: O(n)

    Memory: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxVol = 0

        while l < r:
            currVol = (r - l) * min(height[l], height[r])

            maxVol = max(maxVol, currVol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxVol
