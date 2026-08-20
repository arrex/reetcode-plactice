from typing import List


class Solution:
    """
    Intuition:
        Note that:
        - Any number XOR with itself yields 0
        - Any number XOR with 0 yields itself

        The idea is to take the XOR of all elements in the input
        array. In the event that the outcome is 0, we simply find
        a non-zero element to subtract. If we can't find a non-zero
        elmt, meaning all elmts are 0, then we know it's impossible
        to form a non-zero XOR output.

    Runtime:
        O(n) to compute XOR of all elmts.

        O(n) to check for non-zero elmt.

        Overall, O(n) runtime complexity.

    Memory:
        O(1).
    """

    def longestSubsequence(self, nums: List[int]) -> int:
        # XOR across whole array
        xor, N = 0, len(nums)
        for elmt in nums:
            xor ^= elmt

        if xor:
            return N

        # if XOR of whole array is 0, then find one non-zero elmt
        for elmt in nums:
            if elmt != 0:
                return N - 1

        # case all elmts are 0 in nums
        return 0
