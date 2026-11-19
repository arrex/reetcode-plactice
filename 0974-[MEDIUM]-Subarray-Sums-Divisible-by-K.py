class Solution:
    """
    Intuition:
        We can keep track of the counts of subarrays grouped by remainders.

        The idea is to "rotate" each group whenever we process a new number
        `n`. To start, the group at index 0 indicates the num of subarrays
        whose remainders is 0 i.e divisible by k; at index 1, the subarrays
        whose remainders is 1; etc.

        One way to achieve this rotation is to realize that whenever we add
        the new number, the current remainder of the subarray `x` becomes
        `(x + n) % k`, so we can shift accordingly. However, this would incur
        O(k) cost to each iteration which causes the soln to TLE.

        The better way is to only track `zeroIx` which represents the current
        index of the group whose remainder is 0. This index shifts as we
        process the numbers. For example, it starts at index 0, but if we
        process a new number, it moves to `(0 - n) % k` or `(zeroIx - n) % k`.
        We subtract n from zeroIx to return the complement. For example,
        -1 % 3 = 2 (= 3 - 1). The complement represents the remainder that we
        need such that, if we add n, we get a remainder of 0 i.e. divisible by
        k.

    Runtime:
        O(n) for the linear scan over nums.

    Memory:
        O(k) for the cnt array.
    """

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0
        # bucket counts by remainder
        cnt = [0] * k
        zeroIx = 0

        for n in nums:
            # adjust zero remainder group's ix
            # ask which old remainder becomes divisible by
            # k after adding number n
            zeroIx = (zeroIx - n) % k
            # process new number n as its own subarray
            cnt[(zeroIx + n) % k] += 1
            res += cnt[zeroIx]

        return res
