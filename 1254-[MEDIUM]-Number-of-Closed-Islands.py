class Solution:
    """
    Intuition:
        The only islands that cannot physically be surrounded are
        islands on the edge of the grid. If we clear these, then
        all remaining islands will be surrounded.

    Runtime:
        O(2 * m * n) ~ O(m * n) to iterate over the grid and clear
        all islands touching the edge of the grid. Iteration processes
        each cell once and DFS processes each cell at most once.

        O(2 * m * n) ~ O(m * n) for the second pass over the grid.
        Similar idea (iterations + DFS).

        Overall, O(m * n) runtime.

    Memory:
        The max recursive depth of DFS is m + n, so the memory overhead
        is at worst O(m + n).
    """

    def closedIsland(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= M or col < 0 or col >= N or grid[row][col] != 0:
                return

            grid[row][col] = 2  # leave tombstone

            if row > 0 and grid[row - 1][col] == 0:
                dfs(row - 1, col)

            if row < M - 1 and grid[row + 1][col] == 0:
                dfs(row + 1, col)

            if col > 0 and grid[row][col - 1] == 0:
                dfs(row, col - 1)

            if col < N - 1 and grid[row][col + 1] == 0:
                dfs(row, col + 1)

        # remove islands on edges of grid
        for row in range(M):
            for col in range(N):
                if (row == 0 or row == M - 1 or col == 0 or col == N - 1) and grid[row][col] == 0:
                    dfs(row, col)

        # omit edges since we cleared all islands alr
        res = 0
        for row in range(1, M - 1):
            for col in range(1, N - 1):
                if grid[row][col] == 0:
                    res += 1
                    dfs(row, col)

        return res
