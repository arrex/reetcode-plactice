from collections import deque
from typing import List


class Solution1:
    """
    Intuition:
        We init a queue with the initial entrance coordinates. Then, we use BFS
        to traverse the maze and return the nearest exit. If no exit is found,
        we return -1.

    Notes:
        This solution is not super polished. There definitely is a better way of
        writing it while keeping the main idea.

    Runtime: O(m * n) since each cell is processed at most once

    Memory:
        O(m * n) since the queue holds at most every cell in the maze. Think for
        example of a 1x1 grid.
    """

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "x"
        q = deque([(entrance[0], entrance[1])])
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            for i in range(len(q)):
                i, j = q.popleft()

                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and steps > 0:
                    return steps

                for di, dj in dirs:
                    I, J = i + di, j + dj

                    if 0 <= I < m and 0 <= J < n and maze[I][J] == ".":
                        q.append((I, J))

                        # Leave tombstone
                        maze[I][J] = "x"

                        print("added", I, J)

            steps += 1

        return -1


class Solution2:
    """
    Intuition:
        Same idea as solution 1. Just written in a cleaner way.

    Notes:
        The improvement in runtime can be attributed to subtle factors.

        The main difference is that in this solution, we do not perform boundary checks
        before enqueueing neighbours. This is because unlike solution 1, we moved the
        return block with the termination condition within the iterations to find the
        neighbours. A valid termination is when we get a cell that falls out of bounds.

        Therefore, since we have the termination block checking if the coordinates are
        out of bounds, we know that if we make it past it, then the coordinates fall
        within the bounds of the maze. We can thus enqueue any coordinate pair that makes
        it to this point without checking bounds again, saving us runtime.
    """

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Constants
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        i_0, j_0 = tuple(entrance)
        # Leave tombstone at entrance
        maze[i_0][j_0] = "x"
        # Init queue
        q = deque([(i_0, j_0)])
        # Init result
        steps = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in dirs:
                    I, J = i + di, j + dj

                    if (I < 0 or I == m or J < 0 or J == n) and steps > 0:
                        return steps

                    if 0 <= I < m and 0 <= J < n and maze[I][J] == ".":
                        q.append((I, J))

                        # Leave tombstone
                        maze[I][J] = "x"

            steps += 1

        return -1
