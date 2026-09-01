from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        We start by scanning the matrix to find the starting position.
        At the same time, we can tally up all the litter and assign each
        litter a unique bit mask with its cell coords being the key.
        This is what the first for loop achieves.

        Then, the wording around minimum steps in the problem suggest a
        BFS traversal. Keeping a visited set of all pieces of state (row,
        col, energy left, bit mask of litter collected) causes memory
        limit violation. We need a smarter pruning method. This is where
        the `bestEnergy` matrix comes in. We encode 3 pieces of state to
        form the key when accessing this matrix: row, col, bit mask. For
        each combination, we want to store the most optimal state i.e. the
        highest energy remaining. This is because if we land on the same
        cell having collected the same pieces of litter, but having diff
        energies, then it is strictly better to take the path leading to
        the higher energy remainder.

    Runtime:
        O(M * N) to scan the matrix for litter and starting pos.

        O(M * M * energy * 2^k) where k is the number of litter since we
        need to process every existing state possible in the worst case.

        Overall, O(M * M * energy * 2^k) runtime.

    Memory:
        O(M * M * energy * 2^k) for the BFS queue since it can store up
        to every unique state possible.
    """

    def minMoves(self, classroom: List[str], energy: int) -> int:
        M, N = len(classroom), len(classroom[0])
        sr, sc = 0, 0
        litterCount = 0
        litterMap = {}

        for r in range(M):
            for c in range(N):
                # found starting point
                if classroom[r][c] == "S":
                    sr, sc = r, c
                # found litter
                elif classroom[r][c] == "L":
                    # record unique mask
                    litterMap[(r, c)] = 1 << litterCount
                    litterCount += 1

        # no litter in classroom
        if litterCount == 0:
            return 0

        fullMask = 1 << litterCount
        # matrix to help prune branches
        bestEnergy = [[[-1 for _ in range(fullMask)] for _ in range(N)] for _ in range(M)]
        bestEnergy[sr][sc][0] = energy

        # encode as (row, col, mask, energy remaining, steps)
        q = deque([(sr, sc, 0, energy)])
        steps = 0
        # bfs to find min steps
        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                # collected all litter
                if mask == fullMask - 1:
                    return steps

                # ran out of energy
                if e == 0:
                    continue

                # explore neighbours
                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    # skip out of bounds & obstacles
                    if nr < 0 or nr >= M or nc < 0 or nc >= N or classroom[nr][nc] == "X":
                        continue

                    ne = energy if classroom[nr][nc] == "R" else e - 1
                    nmask = mask | litterMap[(nr, nc)] if classroom[nr][nc] == "L" else mask
                    # prune branches not worth exploring, only append to queue
                    # if we land in same row/col cell with strictly more energy
                    # for the given mask (representing subset of litter collected
                    # so far)
                    if ne > bestEnergy[nr][nc][nmask]:
                        bestEnergy[nr][nc][nmask] = ne
                        q.append((nr, nc, nmask, ne))

            steps += 1

        # impossible to collect all litter
        return -1
