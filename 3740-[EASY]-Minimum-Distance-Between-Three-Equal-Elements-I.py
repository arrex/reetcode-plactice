from collections import defaultdict
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        Brute force approach.

    Runtime:
        O(n^3) since 3 loops.

    Memory:
        O(1).
    """

    def minimumDistance(self, nums: List[int]) -> int:
        # early return for base case
        if len(nums) < 3:
            return -1

        res = inf
        N = len(nums)

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] == nums[j] == nums[k]:
                        res = min(res, abs(i - j) + abs(j - k) + abs(k - i))

        return res if res != inf else -1


class Solution2:
    """
    Intuition:
        We can build a hashmap by keying on each unique value
        in the input `nums` array and storing all the indices
        for that number as the value.

        Then, we can use a sliding window approach to calculate
        min distances across indices if a value has more than
        3 occurrences.

    Runtime:
        O(n) to build the hashtable since we need to process
        each input element.

        O(n) in the worst case to compute the min distance
        using sliding window if all the indices map to the
        same key value (i.e. array of duplicates only).

        Overall, we have O(n) + O(n) which yields O(n).

    Memory:
        O(n) for the hashtable.
    """

    def minimumDistance(self, nums: List[int]) -> int:
        # early return for base case
        if len(nums) < 3:
            return -1

        res = inf

        # build hashmap
        hashmap = defaultdict(list)
        for i, n in enumerate(nums):
            hashmap[n].append(i)

        # search thru lists of indices
        for val in hashmap.values():
            # if given num is not present at at least 3 indices, skip
            if len(val) < 3:
                continue

            # fixed sliding window over indices
            l = 0
            while l < len(val) - 2:
                i, j, k = val[l], val[l + 1], val[l + 2]
                dist = abs(i - j) + abs(j - k) + abs(k - i)
                res = min(res, dist)

                l += 1

        return res if res != inf else -1


class Solution3:
    """
    Intuition:
        Overall the same as Solution2, the only difference
        is to realize that the distance calculation formula
        can be simplified to 2 * abs(k - i).

    Runtime:
        Same as Solution2.

    Memory:
        Same as Solution2.
    """

    def minimumDistance(self, nums: List[int]) -> int:
        # early return for base case
        if len(nums) < 3:
            return -1

        res = inf

        # build hashmap
        hashmap = defaultdict(list)
        for i, n in enumerate(nums):
            hashmap[n].append(i)

        # search thru lists of indices
        for val in hashmap.values():
            # if given num is not present at at least 3 indices, skip
            if len(val) < 3:
                continue

            # fixed sliding window over indices
            l = 0
            while l < len(val) - 2:
                r = l + 2
                dist = abs(val[l] - val[r]) * 2
                res = min(res, dist)

                l += 1

        return res if res != inf else -1
