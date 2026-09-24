from typing import List


class Solution:
    """
    Intuition:
        Do what the problem says.

    Runtime:
        O(n * log_10 k) where n is the num of elmts and k is the largest
        elmt. Using big-O rules, we can simplify this to O(n log k).

    Memory:
        O(1).
    """

    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            digitSum = 0
            curr = n

            while curr:
                rem = curr % 10
                digitSum += rem
                curr //= 10

            if digitSum == i:
                return i

        # no match found
        return -1
