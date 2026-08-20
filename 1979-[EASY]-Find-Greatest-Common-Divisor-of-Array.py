from typing import List


class Solution1:
    """
    Intuition:
        Find the largest and the smallest numbers. Then,
        iterate through all the values between 1 and the
        smallest value inclusively to find the GCD. Std
        brute force approach.

    Runtime:
        O(n) to find the smallest and largest nums.

        Then, O(k) to find the GCD where k is the smallest
        number.

        Overall, O(n + k) runtime.

    Memory:
        O(1).
    """

    def findGCD(self, nums: List[int]) -> int:
        small, large = min(nums), max(nums)
        res = 1

        for i in range(1, small + 1):
            if small % i == 0 and large % i == 0:
                res = i

        return res


class Solution2:
    """
    Intuition:
        Standard implementation of Euclidian's algorithm which
        is the fastest way to find GCD. The intuition is as
        follows:

        Any divisor common to both numbers must also divide the
        remainder, so you can keep replacing the larger number
        with the remainder until nothing is left.

    Runtime:
        O(n) to find largest and smallest numbers.

        O(log K) to find the GCD given small and large nums.

        Overall, O(n + log K).

    Memory:
        O(1).
    """

    def findGCD(self, nums: List[int]) -> int:
        small, large = min(nums), max(nums)

        while small:
            small, large = large % small, small

        return large
