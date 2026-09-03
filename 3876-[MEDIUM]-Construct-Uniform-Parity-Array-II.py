from math import inf


class Solution:
    """
    Intuition:
        The intuition for this problem is similar to the previous variant
        Construct Uniform Array I. We handle all odds or all evens cases
        the same. The only difference is how we handle the case where we
        have both. When we have both, we need the smallers odd number to
        be smaller than the smallest even number. This way, when we subtract,
        the result will not be negative. Otherwise, we cannot construct
        a valid uniform array.

    Runtime:
        O(n) to find smallest odd and even numbers.

    Memory:
        O(1).
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd, minEven = inf, inf
        for n in nums1:
            if n % 2 == 0 and n < minEven:
                minEven = n
            elif n % 2 == 1 and n < minOdd:
                minOdd = n

        # all even or all odd
        if minEven == inf or minOdd == inf:
            return True

        # mix of both
        return minEven > minOdd
