from typing import List


class Solution:
    """
    Intuition:
        Compute the sum of each island and check its divisibilit
        by k.

        We optimize DFS by checking the conditions needed before
        making a recursive call to save overhead.

    Runtime:
        Traversing each cell takes O(m * n).

        DFS calls leave a tombstone at the call site's cell, so
        each cell is processed at most once, leading to O(m * n).

        Overall, O(2 * m * n) ~ O(m * n) runtime.

    Memory:
        O(m + k) as DFS has a max recursive depth of that size.
    """

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(row, col):
            tot = grid[row][col]
            grid[row][col] = 0

            if row > 0 and grid[row - 1][col]:
                tot += dfs(row - 1, col)

            if row < M - 1 and grid[row + 1][col]:
                tot += dfs(row + 1, col)

            if col > 0 and grid[row][col - 1]:
                tot += dfs(row, col - 1)

            if col < N - 1 and grid[row][col + 1]:
                tot += dfs(row, col + 1)

            return tot

        res = 0
        for row in range(M):
            for col in range(N):
                # found an island
                if grid[row][col] > 0:
                    tot = dfs(row, col)

                    if tot % k == 0:
                        res += 1

        return res
