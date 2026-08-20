from collections import Counter
from typing import List


class Solution:
    """
    Intuition:
        Our goal is to compare rows and columns. Instead of brute forcing,
        we can use a hashmap where the key is the row (need immutable data
        type like a tuple) and the value is the frequency of the row (in
        case we have non-unique rows).

        Then, for each column, we check the number of rows that match by
        performing a lookup in our hashmap and increment the result accordingly.

    Runtime:
        O(n^2). Bounded by the nested loop block.

    Memory:
        O(n^2). In the worst case, the 'rows' hashmap contains n rows of
        length n each.
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        res = 0
        rows = Counter(tuple(row) for row in grid)

        for c in range(N):
            col = [grid[r][c] for r in range(N)]
            res += rows[tuple(col)]

        return res
