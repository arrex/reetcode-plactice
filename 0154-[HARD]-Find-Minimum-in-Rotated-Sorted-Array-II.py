from typing import List


class Solution1:
    """
    Intuition:
        The intuition remains vastly the same as the previous version
        of this question (leetcode #153). The crux of this problem is
        how to tackle duplicates.

        The addition we introduce is to skip duplicates at either sides
        of the interval bounded by the l & r ptrs. By eliminating these
        duplicates, we remove the ambiguity and can easily determine if
        either partition is properly sorted.

    Runtime:
        O(n) since in the worst case, we have an array containing only
        duplicates.

    Memory:
        O(1) since we only use ptrs.
    """

    def findMin(self, nums: List[int]) -> int:
        N = len(nums)

        l, r = 0, N - 1
        while l < r:
            # adjust left and right ptrs to skip duplicates
            while l < N - 1 and nums[l] == nums[l + 1]:
                l += 1

            while r > 0 and nums[r] == nums[r - 1]:
                r -= 1

            # binary search sequence
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]


class Solution2:
    """
    Intuition:
        The intuition of this solution is virtually identical to Solution
        1. However, there is a key optimization. Solution 1 seeks to trim
        duplicates on both sides of the interval, but this is overkill.

        The mental model surrounding solving this problem revolves around
        asking if the given half is sorted or not. With that in mind, we
        only really need to trim duplicates on one side!

    Runtime:
        O(n) in the worst case still.

    Memory:
        Still O(1).
    """

    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:  # nums[mid] == nums[r] i.e. we have duplicates
                r -= 1

        return nums[l]
