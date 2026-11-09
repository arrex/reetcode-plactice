class Solution:
    """
    Intuition:
        Use a dp approach. For a given position, we can either have come from
        the top or the left since the problem specifies we can only travel right
        or down.

        As such, we can count the number of paths at each cell by summing the
        number of paths at (r - 1, c) and (r, c - 1). For cells with obstacles,
        we simply skip this computation.

    Runtime:
        Initializing the dp cache takes O(m * n) time.

        The core loop takes O(m * n) time.

        Overall, we have O(m * n) runtime.

    Memory:
        O(m * n) for the dp cache.
    """

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]

        for r in range(M):
            for c in range(N):
                # base case
                if r == 0 and c == 0:
                    dp[r][c] = 1
                    continue

                # obstacle:
                if obstacleGrid[r][c] == 1:
                    continue
                else:
                    numWays = 0

                    if r > 0:
                        numWays += dp[r - 1][c]

                    if c > 0:
                        numWays += dp[r][c - 1]

                    dp[r][c] = numWays

        return dp[-1][-1]
