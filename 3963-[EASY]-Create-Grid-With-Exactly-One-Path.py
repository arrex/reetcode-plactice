class Solution:
    """
    Intuition:
        The easiest valid path to create is all the way
        down, then all the way to the right.

    Runtime:
        O(m * n) to create the grid.

    Memory:
        O(m * n) if you count result, otherwise O(1)
        auxiliary memory complexity.
    """

    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." + "#" * (n - 1) for _ in range(m - 1)] + ["." * n]
