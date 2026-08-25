from typing import List


class Solution:
    """
    Intuition:
        We maintain an index at which we insert. We only increment
        this index when we encounter an elmt not equal to `val`.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        ix = 0

        for n in nums:
            if n != val:
                nums[ix] = n
                ix += 1

        return ix
