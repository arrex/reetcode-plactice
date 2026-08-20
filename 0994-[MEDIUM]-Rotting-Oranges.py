from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        Standard multi-source BFS question. The only key observation is
        that our termination condition for BFS is either when there is
        nothing left to process in the queue or if we ran out of fresh
        oranges to rot.

    Runtime: O(m * n) -> bounded by finding rotten orange sources.

    Memory: O(m * n)
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        numFresh = 0
        q = deque()

        # Find all rotten oranges and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        # If no fresh oranges on the grid
        if numFresh == 0:
            return 0

        # Start time at -1 since we spend an extra iteration
        # processing default rotten oranges
        time = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        while q and numFresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc

                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        # Rot neighbouring orange
                        grid[row][col] = 2
                        numFresh -= 1
                        # Add neighbour to queue
                        q.append((row, col))

            time += 1

        return time if numFresh == 0 else -1
