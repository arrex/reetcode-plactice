class Solution:
    """
    Intuition:
        The key observation is to notice that odd + even = odd, that even + even = even, and
        that odd + odd = even.

        We track the number of even and odd subarrays that end at ix - 1 (i.e. ix - 1 relative
        to `num` since we loop by value). If the subsequent elmt is odd, then the count of odd
        subarray sums is equal to the number of even subarray sums plus the new elmt itself. If
        the subsequent elmt is even, then the count of odd sum subarrays stays the same, but
        we can consider the value itself as a subarray so we increment the count of even sum
        subarrays by 1.

    Runtime:
        O(n) for a linear pass on input array `arr`.

    Memory:
        O(1).
    """

    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odds = evens = res = 0

        for num in arr:
            if num % 2 == 1:
                odds, evens = evens + 1, odds
            else:
                evens += 1

            res += odds

        return res % MOD
