from typing import List


class Solution:
    """
    Intuition:
        Hash the nums array into a set to optimize lookup time. Then,
        iterate until we find missing multiple.

    Runtime:
        O(n) time to hash the input array into a set.

        O(n) to find the missing multiple since our set contains at
        most n distinct multiples.

        Overall, O(n) runtime.

    Memory:
        O(n) for the hashset.
    """

    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        curr = k

        while curr in nums:
            curr += k

        return curr
