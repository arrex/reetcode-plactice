class Solution:
    """
    Intuition:
        We have 3 cases to consider.

        If the array is full of odd numbers, then we just return the
        same array.

        If the array if full of even numbers, then we also just return
        the same array.

        If the array contains both, then we can construct an array such
        that every elmt is odd since the difference between an even and
        odd number is odd.

        By this principle, we can construct an array of all even or all
        odd numbers for any input.

    Runtime:
        O(1).

    Memory:
        O(1).
    """

    def uniformArray(self, nums1: list[int]) -> bool:
        return True
