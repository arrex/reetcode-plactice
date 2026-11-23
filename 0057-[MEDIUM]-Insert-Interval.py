import bisect


class Solution:
    """
    Intuition:
        Use binary search to find the insertion point of the new interval, then
        the problem just boils down to merging intervals.

        Note that we save ourselves the work from sorting as inserting using binary
        search guarantees sorted order.

    Runtime:
        O(log n) to find the insertion index.

        O(n) to process all intervals and merge overlapped ones.

        Overall, O(n) runtime.

    Memory:
        O(1) auxiliary space, O(n) with the merged array.
    """

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # binary search to find insertion
        insertIx = bisect.bisect_left(intervals, newInterval)

        # still in sorted order by start time
        intervals = intervals[:insertIx] + [newInterval] + intervals[insertIx:]

        # merge intervals
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = merged[-1][1]

            if prevEnd < start:  # case: disjoint
                merged.append([start, end])
            else:  # case: overlap
                merged[-1][1] = max(end, prevEnd)

        return merged
