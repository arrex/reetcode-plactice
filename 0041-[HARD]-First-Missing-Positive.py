from typing import List


class Solution:
    """
    Intuition:
        In a brute force solution, we would hash all the elements and iterate until
        we find the missing integer.

        We can take that idea and apply it to our O(1) memory constraint. The idea
        is the input array becomes our "hashtable". We scan through all the elements
        and slot them into their correct slots by performing swaps. This way, the
        positive integers in our input will be slotted in increasing order.

        We then use a second pass to scan for the first hole or missing integer and
        return its value.

    Runtime:
        O(n) to perform all swaps.

        O(n) to find the missing integer.

        Overall, O(n) runtime.

    Memory:
        O(1).
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        ix = 0
        while ix < len(nums):
            # skip non-positive and out of bounds and already in right position and duplicates
            if (
                nums[ix] <= 0
                or nums[ix] > len(nums)
                or nums[ix] == ix + 1
                or nums[nums[ix] - 1] == nums[ix]
            ):
                ix += 1
                continue

            # swap curr elmt to its respective slot
            # and elmt at destination to curr ix
            n = nums[ix]
            nums[ix], nums[n - 1] = nums[n - 1], nums[ix]

        # find missing integer
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        # everything is present, missing must be next in sequence
        return len(nums) + 1
