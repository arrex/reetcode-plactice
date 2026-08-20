from typing import List


class Solution1:
    """
    Intuition:
        We can use a dynamic sliding window approach to solve this problem. Our
        condition is that our window can only ever contain a singular item to delete
        i.e. a 0. We encode this in a boolean flag called 'hasDeleted'. If our
        window only contains 1's, we can check if the flag was toggled at the end
        and decrement if it has not since we are forced to delete one element.

        Our algorithm will operate based on these 3 main cases:
        1) When we hit a 1, we increment our current length and adjust 'res' accordingly.
        2) When we hit a 0 and the hasDeleted flag is false, we toggle the flag and
           continue
        3) When we hit a 0 and the hasDeleted flag is true, we need to increment the
           left pointer until we clear the leftmost 0.

    Runtime:
        O(n) -> one pass

    Memory:
        O(1) -> only ptrs

    Notes:
        The following solution breaks down the cases very distinctly. We can definitely
        rewrite the solution to be a bit more elegant.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        hasDeleted = False
        l, r = 0, 0
        curr, res = 0, 0

        while r < len(nums):
            if nums[r] == 1:
                curr += 1

                res = max(res, curr)
            else:
                if not hasDeleted:
                    hasDeleted = True
                else:
                    while nums[l] != 0:
                        curr -= 1
                        l += 1

                    l += 1

            r += 1

        return res if hasDeleted else res - 1


class Solution2:
    """
    Notes:
        Exact same intuition, runtime and memory as Solution1. Just rewritten
        to reduce the nested if-else blocks.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        hasDeleted = False
        l, r = 0, 0
        curr, res = 0, 0

        while r < len(nums):
            if nums[r] == 1:
                curr += 1

                res = max(res, curr)
            elif not hasDeleted:
                hasDeleted = True
            else:
                while nums[l] != 0:
                    curr -= 1
                    l += 1

                l += 1

            r += 1

        return res if hasDeleted else res - 1
