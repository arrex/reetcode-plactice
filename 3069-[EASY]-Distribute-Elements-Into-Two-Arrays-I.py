class Solution:
    """
    Intuition:
        Trivial, problem description outlines sequence of operations.

    Runtime:
        O(n) to process each elmt in the input `nums`.

    Memory:
        O(n) since `arr1` and `arr2` contain the same number of elmts
        as `nums`.
    """

    def resultArray(self, nums: list[int]) -> list[int]:
        arr1, arr2 = [nums[0]], [nums[1]]

        for n in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)

        return arr1 + arr2
