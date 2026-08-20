from collections import defaultdict
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        We sort the array to minimize the elements wit respect
        to their neighbors. This also sets up our fixed sliding
        window approach later.

        E.g. [4, 1, 2] vs [1, 2, 4]

        Once the array is sorted, we can use a hasmap with the
        key representing the distance between 2 values. We then
        go through every pair of elements using a fixed window
        of size 2 and compute the distance. We also keep track
        of the min distance to return our final result.

    Runtime:
        Sorting the array takes O(n * log n).

        Building the hashmap takes O(n).

        Overall O(n * log n) time.

    Memory:
        Sorting in place costs O(n) in the worst case (according
        to Gemini quick summary...).

        The hashmap takes O(n) space.

        Overall, O(n) space.
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = inf

        # hashmap -- key on diff
        hashmap = defaultdict(list)
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = abs(a - b)
            hashmap[diff].append([a, b])
            minDiff = min(minDiff, diff)

        return hashmap[minDiff]


class Solution2:
    """
    Intuition:
        We can ditcht the hashmap because it overcomplicates
        the problem. Instead, the key observation is that
        whatever we store in result gets wiped if we encounter
        a new minimum.

        Therefore, we just reset the result array whenever we
        encounter a lower difference. Then, we only append to
        the result if the difference is equivalent to the min
        difference.

    Runtime:
        Still O(n * log n) since we have to sort the input array.

    Memort:
        Still O(n) since we have to sort the array in place.
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []

        arr.sort()

        minDiff = inf
        res = []
        prev = arr[0]

        for n in arr[1:]:
            currDiff = n - prev

            # found new min abs diff
            if currDiff < minDiff:
                minDiff = currDiff
                res = []

            if currDiff == minDiff:
                res.append([prev, n])

            prev = n

        return res
