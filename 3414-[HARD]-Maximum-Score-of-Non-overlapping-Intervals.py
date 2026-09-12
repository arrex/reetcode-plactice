from typing import List


class Solution:
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
