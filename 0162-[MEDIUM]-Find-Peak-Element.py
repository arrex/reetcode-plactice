from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        We iterate through each element and compare them to their immediate neighbours. Since the
        constraints tell us that each element is unique, we can perform a strictly greater than comparison.

        We append -inf at the front and back to cover the edge cases where the peak is the first/last
        element in the array.

    Runtime:
        O(n)

    Memory:
        O(1) auxiliary since the array is given as input.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [-inf]

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1


class Solution2:
    """
    Intuition:
        We generally use binary search when we either have a sorted array or want to split an array into
        halves to reduce our search space. Here, the array is not sorted, but we are asked to provide a
        log n solution which hints at reducing the search space in half at each iteration.

        We are told we can return any peak. Therefore, we can use a classic binary search approach and
        check around the mid pointer.

        If the right neighbour (mid + 1) of the mid pointer is smaller, then we know that the peak is
        either at the mid pointer or on its left. Therefore, we can continue searching in the left half.

        Conversely, if the right neighbour is greater than the mid pointer, then we know the peak is
        on the right side.

    Runtime:
        O(log n)

    Memory:
        O(1)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l
