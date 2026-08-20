from collections import defaultdict
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        See intuition for problem 3740, Solution 2 & 3.

    Runtime:
        O(n) to build hashmap.

        O(n) to traverse through all indices for a given
        distance.

        Overall, O(n) time.

    Memory:
        O(n) for the hashmap.
    """

    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        # build hashmap -- key on value
        hashmap = defaultdict(list)
        for ix, n in enumerate(nums):
            hashmap[n].append(ix)

        # compute min dist of good tuple
        minDist = inf
        for indices in hashmap.values():
            # can't form a good tuple
            if len(indices) < 3:
                continue

            # fixed sliding window -- size 3
            for l in range(len(indices) - 2):
                r = l + 2
                dist = abs(indices[l] - indices[r]) * 2
                minDist = min(minDist, dist)

        return minDist if minDist != inf else -1


class Solution2:
    """
    Intuition:
        We can keep track of 2 hashmaps. 1 for the last index of an
        encountered number and another for the index previous to the
        last one.

        While looping through the input, we update both hashmaps
        accordingly. Whenever we match on an element existing in
        `prevprev`, then we know we should compute if the distance is
        a new min.

    Runtime:
        O(n) since every element in the input array is processed once.

    Memory:
        O(n) space for the `prev` hashmap.

        O(n) space for the `prevprev` hashmap. Feel like this is a very
        loose upper bound since it will never be as populated as `prev`
        due to it requiring its elements to have frequency 2. So I guess
        O(n / 2) ~ O(n).

        Overall, O(n) space.
    """

    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        prev = {}
        prevprev = {}
        res = inf

        for i, n in enumerate(nums):
            if n in prevprev:
                k = prevprev[n]
                dist = 2 * abs(i - k)
                res = min(res, dist)

                prevprev[n] = prev[n]
                prev[n] = i
            elif n in prev:
                prevprev[n] = prev[n]
                prev[n] = i
            else:
                prev[n] = i

        if res == inf:
            return -1
        else:
            return res
