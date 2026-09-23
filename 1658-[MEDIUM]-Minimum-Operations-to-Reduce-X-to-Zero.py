class Solution:
    """
    Intuition:
        The key observation is to think in reverse. Instead of finding the min
        prefix + suffix, we find the maximum subarray.

        Thus, our target sum becomes the total sum of the array minus the target
        number x. The problem becomes a dynamic sliding window problem where we
        search for the longest subarray whose sum is equal to this new target.

    Runtime:
        O(n) to sum all the elmts in nums.

        O(n) for our sliding window pass.

        Overall, O(n) time.

    Memory:
        O(1).
    """

    def minOperations(self, nums: list[int], x: int) -> int:
        N = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return N

        l, r = 0, 0
        longest = -1
        currSum = 0
        while r < N:
            # update window sum
            currSum += nums[r]

            # adjust window
            while l < r and currSum > target:
                currSum -= nums[l]
                l += 1

            # update res
            if currSum == target and r - l + 1 > longest:
                longest = r - l + 1

            # increment window
            r += 1

        return -1 if longest == -1 else N - longest
