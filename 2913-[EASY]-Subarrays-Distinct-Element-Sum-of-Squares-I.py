from typing import List


class Solution:
    """
    Intuition:
        Pretty brute force approach. Use a set to keep track
        of unique values across all subarrays. A more runtime
        efficinet solution would involve a segment tree.

    Runtime:
        O(n^2) for the nested loop.

    Memory:
        O(n) for the hashset.
    """

    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            seen = set()

            for j in range(i, N):
                seen.add(nums[j])
                res += len(seen) ** 2

        return res
