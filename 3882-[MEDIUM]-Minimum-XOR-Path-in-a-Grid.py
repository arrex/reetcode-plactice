class Solution:
    """
    Intuition:
        We use a 3D dp cache to encode dp[r][c][n] as "is it possible
        to get XOR value n at grid row r and col c?".

        Then, populate base case and build on top of it.

    Runtime:
        Initializing the dp cache takes O(1024 * m * n) ~ O(m * n) time.

        Each cell requires us to look at (r - 1, c) and (r, c - 1)'s cache
        state, giving 2 * 1024 = 2048 lookups. This means the runtime to
        traverse the whole grid is O(2048 * m * n) ~ O(m * n).

        Finding the smallest XOR value at the destination cell in the grid
        takes up to O(1024) ~ O(1) time.

        Overall, we have a runtime of O(m * n).

    Memory:
        O(1024 * m * n) ~ O(m * n) for the dp cache.
    """

    def minCost(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[[False] * 1024 for _ in range(N)] for _ in range(M)]

        for r in range(M):
            for c in range(N):
                curr = grid[r][c]

                # base case
                if r == 0 and c == 0:
                    dp[0][0][curr] = True
                    continue

                # look up
                if r > 0:
                    for x in range(1024):
                        if dp[r - 1][c][x]:
                            dp[r][c][curr ^ x] = True

                # look left
                if c > 0:
                    for x in range(1024):
                        if dp[r][c - 1][x]:
                            dp[r][c][curr ^ x] = True

        for x, valid in enumerate(dp[M - 1][N - 1]):
            if valid:
                return x

        # should never get here
        return -1
