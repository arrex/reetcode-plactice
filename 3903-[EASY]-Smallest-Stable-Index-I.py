class Solution:
    """
    Intuition:
        The problem is essentially asking us to find the largest elmt
        on the left side of a given index and the smallest elmt on the
        right side of the index.

        We can do this efficiently via 2 linear scans. The first one
        from left to right to find the max elmt on the left partition
        for each index. Then, we scan right to left to find the smallest
        elmt on the right partition of each index.

    Runtime:
        O(n) overall given we have 3 linear scans.

    Memory:
        O(n) for the output, O(1) auxiliary.
    """

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        inst = [0] * len(nums)

        # scan left to right
        large = 0
        for i in range(len(nums)):
            large = max(large, nums[i])
            inst[i] = large

        # scan right to left
        small = large
        for i in range(len(nums) - 1, -1, -1):
            small = min(small, nums[i])
            inst[i] -= small

        # find smallest index satisfying condition
        for i, score in enumerate(inst):
            if score <= k:
                return i

        # no soln found
        return -1
