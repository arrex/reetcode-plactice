from typing import List


class Solution1:
    """
    Intuition:
        A sequence always starts with a number and ends with a number.
        In our case, we are trying to isolate a consecutive sequence. The
        idea is to find the starting number of a sequence and iterate
        until we exhaust it.

        Our starting condition is essentially to check if the number
        previous to it is in the hash set. If it is not, it is a potential
        starter to a sequence.

    Runtime:
        O(n) -> One pass to hash all nums, one pass to find longest streak.

    Memory:
        O(n) -> Need hashset to store all nums in input array.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            # Found smallest
            if n - 1 not in nums:
                currStreak = 1
                currNum = n

                while currNum + 1 in nums:
                    currStreak += 1
                    currNum += 1

                longest = max(longest, currStreak)

        return longest


class Solution2:
    """
    Intuition:
        Same as Solution1. We introduce an optimization and rewrite the solution
        to be a bit more elegant.

    Runtime:
        O(n)

    Memory:
        O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        res = 0

        for n in nums:
            # can't be start of sequence
            if n - 1 in nums:
                continue

            # we have start of a sequence
            curr = n
            while curr + 1 in nums:
                curr += 1

            res = max(res, curr - n + 1)

            # optimization
            if res * 2 >= len(nums):
                break

        return res
