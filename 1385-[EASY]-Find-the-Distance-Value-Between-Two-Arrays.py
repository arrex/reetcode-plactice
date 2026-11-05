import bisect


class Solution:
    """
    Intuition:
        Brute force solution is trivial.

        We can sort the second array and use binary search to find bounds
        for the window containing elmts violating the distance condition.

        If the window is empty, then we have a valid number.

    Runtime:
        Suppose arr1 has len n and arr2 has len m.

        Sorting arr2 takes O(m log m).

        Each iteration incurs 2 binary search calls. Each takes O(log m) time.
        With n iterations, the runtime is O(n log m).

        So the overall runtime is O(m log m + n log m).

    Memory:
        O(1).
    """

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()

        res = 0
        for n in arr1:
            # find window of candidates violating distance
            l = bisect.bisect_left(arr2, n - d)
            r = bisect.bisect_right(arr2, n + d)

            # window is empty = no elmt s.t. diff <= dist
            if r == l:
                res += 1

        return res
