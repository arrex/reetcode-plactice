from typing import List


class Solution:
    """
    Intuition:
        There are 3 scenarios in which we can perform all the deletions:
        - We remove both min and max by only consuming from the front
        - We remove both min and max by only consuming from the back
        - We remove both min and max by consuming from both ends

        The problem becomes which scenario yields the lowest amount of
        deletions.

    Runtime:
        O(n) to find the max and min and their respective indices.

        O(1) to compute the rest.

        Overall, O(n) runtime.

    Memory:
        O(1).
    """

    def minimumDeletions(self, nums: List[int]) -> int:
        # find indices of elmts of interest
        minIx, maxIx = 0, 0
        for i in range(len(nums)):
            if nums[i] < nums[minIx]:
                minIx = i
            if nums[i] > nums[maxIx]:
                maxIx = i

        # we don't care which index represents min or max,
        # just care about which one is left or right boundary
        l = min(minIx, maxIx)
        r = max(minIx, maxIx)

        return min(
            # just from front
            r + 1,
            # just from back
            len(nums) - l,
            # both sides
            (l + 1) + (len(nums) - r),
        )
