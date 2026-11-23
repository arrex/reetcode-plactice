class Solution:
    """
    Intuition:
        Sort the intervals by start time.

        Then we process in order. We distinguish between 2 cases: the intervals
        are disjoint and the intervals overlap.

        If they are disjoint, we simply append the new interval.

        If they overlap (the two subcases being total and partial overlap), we
        take the end time of the last interval in merged to become the max of
        the previous end time and the current end time.

    Runtime:
        O(n log n) to sort.

        O(n) to linearly process intervals.

    Memory:
        O(1) auxiliary memory, omitting the merged array which is O(n).
    """

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            prevEnd = merged[-1][1]

            if start > prevEnd:  # case: disjoint
                merged.append([start, end])
            else:  # case: overlap
                merged[-1][1] = max(prevEnd, end)

        return merged
