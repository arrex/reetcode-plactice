class Solution:
    """
    Intuition:
        Sort the array and enumerate through each entry.

    Runtime:
        O(n log n) to sort.

        O(n) for the enumeration pass.

        Overall, O(n log n) runtime.

    Memory:
        O(1) auxiliary memory since sort happens in place.

        O(n) memory for the res array.
    """

    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []

        for i, n in enumerate(sorted(nums)):
            if n == target:
                res.append(i)

        return res
