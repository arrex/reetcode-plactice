from typing import List


class Solution:
    """
    Intuition:
        We maintain 2 ptrs. The left ptr represents the one at which we
        insert elements. The right ptr represents the one we scan the
        input array with.

        Whenever we hit a duplicate, we increment the traversal right ptr.

        Whenever we hit a new elmt, we increment the left ptr and insert
        the elmt.

    Runtime:
        O(n) to scan the entire input array and perform insertions.

    Memory:
        O(1) since we only have 2 ptrs.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]

        return l + 1
