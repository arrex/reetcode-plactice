from bisect import bisect_right
from typing import List


class Solution1:
    """
    Intuition:
        Brute force approach. We try to come up with every single combination of 1 to 4
        intervals.

        Having 4 hard-coded loops forces us to only consider solutions where we choose
        4 intervals. Some inputs might not have 4 non-overlapping intervals. As such,
        we need to consider solutions where we choose up to 4 intervals (i.e. 1 or 2
        or 3 or 4), so we opt for backtracking.

        Note that this solution does not pass all test cases and fails TLE... :(

    Runtime:
        We have n candidates where we only choose 1 interval.

        We have n^2 candidates where we choose 2 intervals.

        We have n^3 candidates where we choose 3 intervals.

        We have n^4 candidates where we choose 4 intervals.

        Thus, we have a total of n + n^2 + n^3 + n^4. The n^4 term dominates, so the
        runtime is O(n^4).

    Memory:
        The depth of our backtracking recursion tree is capped at 4 here since we
        choose at most 4 intervals. Thus, the memory complexity is O(4) ~ O(1).
    """

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        res = []
        maxScore = 0

        def backtrack(pos: int, chosen: List[int], score: int):
            nonlocal res, maxScore

            # check every single set of chosen indices (not just sets of 4 indices)
            if score > maxScore:
                maxScore = score
                res = chosen.copy()
            elif score == maxScore and chosen < res:
                res = chosen.copy()

            # nothing left to consume
            if pos == len(intervals) - 1:
                return

            # chose 4 intervals
            if len(chosen) == 4:
                return

            for i in range(pos + 1, len(intervals)):
                il, ir, iw = intervals[i]

                valid = True
                for c in chosen:
                    cl, cr, _ = intervals[c]

                    # there is overlap
                    # the condition is essentially non-overlapping checks + de morgan's law
                    if (not cl > ir) and (not cr < il):
                        valid = False
                        break

                if valid:
                    chosen.append(i)
                    backtrack(i, chosen, score + iw)
                    chosen.pop()

        for i, interval in enumerate(intervals):
            backtrack(i, [i], interval[2])

        return res


class Solution2:
    """
    Intuition:
        We can optimize the structure of our previous soln by using dp.

        We employ a bottom-up dp soln where our pieces of state are the max score
        and the number of remaining choices. More precisely, dp[i][j] answers what
        the max score score is within the suffix intervals[i:] with j remaining
        choices to make.

        We sort our intervals by start position such that for a given interval, we
        can leverage binary search to find the immediate next non-overlapping
        interval. Since we are sorting the intervals, we need to persist their original
        index as well.

        We sort by start and iterate backwards to satisfy the non- overlapping
        constraint. The index `target` defines the start of the suffix in the input
        intervals i.e. intervals[target:] that contains all the valid candidates.
        The dp cache tells us the best combination to take within that suffix.

    Runtime:
        O(n) to attach the original index to each interval.

        O(n log n) to sort all the intervals by start.

        O(n) to init the base cases in the dp cache.

        O(n) to populate the cache.

        Overall, O(n) runtime.

    Memory:
        O(5 * n) ~ O(n) for the cache.
    """

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)

        # attach original index to each interval
        for i, interval in enumerate(intervals):
            interval.append(i)

        # sort intervals based on start pos
        intervals = sorted(intervals, key=lambda i: i[0])

        # dp[i][j] max score in intervals[i:] with up to j interval choices remaining
        #
        # we store tuple of (score, chosen indices) where chosen indices is a list
        dp = [[(0, ())] * 5 for _ in range(N + 1)]

        # base case: 0 remaining choices -> contribute nothing
        for i in range(N + 1):
            dp[i][0] = (0, ())
        # base case: no more available intervals -> contributes nothing
        for j in range(5):
            dp[N][j] = (0, ())

        # populate cache
        for i in range(N - 1, -1, -1):
            _, currR, currW, ogIx = intervals[i]
            # store ix of first next non-overlapping interval for take case
            target = bisect_right(intervals, currR, key=lambda i: i[0])

            for j in range(1, 5):
                # case take: find first non-overlapping interval
                takeScore = dp[target][j - 1][0] + currW
                takeIndices = tuple(sorted(dp[target][j - 1][1] + (ogIx,)))

                # case skip: simply take max score from i + 1 with same num of remaining choices
                skipScore = dp[i + 1][j][0]
                skipIndices = dp[i + 1][j][1]

                if takeScore > skipScore:
                    dp[i][j] = (takeScore, takeIndices)
                elif skipScore > takeScore:
                    dp[i][j] = (skipScore, skipIndices)
                # takeScore == skipScore, tie-break by lexicographically smallest
                else:
                    dp[i][j] = (skipScore, min(takeIndices, skipIndices))

        return list(dp[0][4][1])
