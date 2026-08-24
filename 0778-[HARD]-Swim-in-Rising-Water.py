import heapq
from typing import List


class Solution:
    """
    Intuition:
        Since we want to find the minimum time to traverse the grid,
        we can use Dijkstra's to sort paths by time. For each path,
        we track its current time and the current cell.

        Whenever we process a cell, we can keep exploring as long as
        the elevations are less than or equal to the current time.

        If the elevation is greater than the current time, we need to
        wait until the time = elevation to swim to the next cell.

        Note that we have to start time at grid[0][0].

    Runtime:
        We have M * N cells in total. Each one is processed at most
        once. Adding a cell to our priority queue takes log time.

        Thus, the overall runtime is O((M * N) * log (M * N)).

    Memory:
        The priority queue holds at most all cells, meaning O(M * N)
        memory.

        The seen set also holds at most all cells which takes O(M * N).

        Thus, the overall memory complexity is O(M * N).
    """

    def swimInWater(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # encode as (elevation, (r, c))
        pq = [(grid[0][0], (0, 0))]
        seen = {(0, 0)}
        while pq:
            time, (r, c) = heapq.heappop(pq)

            # reached bottom right corner
            if r == M - 1 and c == N - 1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # in bounds
                if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    elev = grid[nr][nc]

                    # we can advance without incrementing time`
                    if elev <= time:
                        heapq.heappush(pq, (time, (nr, nc)))
                    else:  # we need to wait for the water level to rise
                        heapq.heappush(pq, (elev, (nr, nc)))

        # should never get here
        return -1
