from math import inf
from typing import List


class Solution:
    """
    Intuition:
        Same general intuition as 3Sum, but we might not find an exact
        match. For that, we just keep track of the min diff encountered
        so far and update the result whenever we encounter a smaller one.

    Runtime:
        O(n log n) to sort.

        O(n^2) to find the closest triplet since we have n iterations of
        the for-loop and each iteration costs at most O(n) with l,r ptrs
        traversing the entire array.

    Memory:
        O(1).
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        minDiff = inf
        res = nums[0] + nums[1] + nums[2]

        nums.sort()

        for i in range(N):
            l, r = i + 1, N - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                diff = abs(target - currSum)
                if diff < minDiff:
                    minDiff = diff
                    res = currSum

                # found exact match, no need to keep searching
                if currSum == target:
                    return currSum
                elif currSum < target:
                    l += 1
                else:
                    r -= 1

        return res
