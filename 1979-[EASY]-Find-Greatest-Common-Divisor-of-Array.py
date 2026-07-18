class Solution:
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

    def findGCD(self, nums: list[int]) -> int:
        small, large = min(nums), max(nums)
        res = 1

        for i in range(1, small + 1):
            if small % i == 0 and large % i == 0:
                res = i

        return res
