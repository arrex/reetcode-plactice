from math import inf
from typing import List


class Solution:
    """
    Intuition:
        The key observation is that if our window is defined by indices l and r,
        and that r % k = l % k, then we know we have a subarray length divisible
        by k.

        As such, whenever we hit a right boundary r where r % k = 3, for example, we
        can look at all previous indices l where l % k = 3 as well to define a sub-
        array with length divisible by k.

        We combine this idea with prefix sums. If we compute the prefix sum at l and
        the prefix sum at r, we can easily find the sum of the window by performing
        `prefix sum at l - prefix sum at r`.

        If we use a greedy approach, we can keep track of the minimum prefix sum for
        each remainder value in [0...k-1]. Then, on subsequent hits for the same
        remainder, we can subtract this min prefix sum to maximize our window sum.
        The visualization is essentially to think of forming a valid length sub-
        array by taking all elmts up to index r and then chopping off the prefix
        of the arr up to index l.

    Runtime:
        O(n) as we process each elmt once.

    Memory:
        O(k) for the minPrefix array tracking smallest prefix sums bucketed by length
        remainder.
    """

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # holds min subarray sum bucketed by remainders
        minPrefix = [inf] * k
        # base case: smallest sum for subarr whose len divisible by k is empty subarr
        minPrefix[0] = 0
        res = -inf
        prefix = 0
        for i, n in enumerate(nums):
            prefix += n
            rem = (i + 1) % k

            # window sum = curr prefix sum - smallest sum subarr in same remainder bucket we can chop off
            if prefix - minPrefix[rem] > res:
                res = prefix - minPrefix[rem]

            # check if curr prefix subarr w len % k = rem has smaller sum
            if prefix < minPrefix[rem]:
                minPrefix[rem] = prefix

        return res
