from math import inf


class Solution:
    """
    Intuition:
        Intuitively, using a dynamic sliding window approach
        seems very natural to this question. It can keep track
        of a sum within the current subarray window and we can
        expand/adjust it easily.

        Except, we also have a non-overlapping constraint to
        satisfy. Sliding window on its own is not enough to
        solve this problem. We need to "remember" what the
        previous shortest subarray whose sum is equal to target
        is.

        This is where dp can come in. We can build a cache where
        dp[i] stores the shortest non-overlapping subarray before
        index i (before to help satisfy the non-overlapping
        condition).

    Runtime:
        Each elmt in the input array is processed up to twice
        (once while expanding window, and up to once while
        increment the left ptr). This means the runtime of
        our solution is O(2n) ~ O(n).

    Memory:
        O(n) for the dp cache.
    """

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        N, res, currSum = len(arr), inf, 0
        # dp[i] answers shortest subarray w sum eq to target
        # in arr[:i] i.e. before index i
        dp = [inf] * (N + 1)

        l = 0
        for r, x in enumerate(arr):
            # expand window
            currSum += x

            # adjust window
            while currSum > target:
                currSum -= arr[l]
                l += 1

            # update cache
            if currSum == target:
                # case: we have found new subarray
                # subarray [l, r] eq target
                # add its len r - l + 1 to best len
                # before index l i.e. dp[l]
                res = min(res, r - l + 1 + dp[l])
                dp[r + 1] = min(dp[r], r - l + 1)
            else:
                # case: subarray sum not eq to target yet
                # carry forward previous best
                dp[r + 1] = dp[r]

        return -1 if res == inf else res
