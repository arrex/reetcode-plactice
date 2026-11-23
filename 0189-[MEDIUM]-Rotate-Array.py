class Solution:
    """
    Intuition
        The key observation is that reversersing a list twice restores its order.

        We can use this observation to our advantage. First, we will reverse the
        entire list.

        Then, we will reverse the first k elmts. After one reversal, they contain
        the last k elmts in reversed order. If we reverse them again, their original
        order is restored.

        Then, we restore the ordering for the rest of the array as well.

        The result is that we have the rotated array with the tail (last k elmts)
        at the head now and the rest of the array shifted by k steps.

    Runtime:
        O(n) + O(k) + O(n - k) = O(2 * n) ~ O(n) for all 3 loops.

    Memory:
        O(1).
    """

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N

        if k == 0:
            return

        l, r = 0, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
