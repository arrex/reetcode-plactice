from collections import Counter
from typing import List


class Solution1:
    """
    Intuition:
        Brute force approach using a fixed sliding window. We process
        each subarray and maintain a hashmap to count frequencies.

    Runtime:
        O(n * k) since we process each elmt in the input list `nums`
        and we also have a nested loop that iterates through the
        entire window of size k.

    Memory:
        O(n) for the `counter` hashmap.
    """

    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = {}
        l, r = 0, k - 1

        while r < len(nums):
            # keep a set to avoid double counting the same elmt
            # consider nums = [2, 2], k = 2
            elmts = set()

            for i in range(l, r + 1):
                n = nums[i]
                elmts.add(n)

            for e in elmts:
                if e not in counter:
                    counter[e] = 0

                counter[e] += 1

            l += 1
            r += 1

        # find res
        res = -1
        for n, freq in counter.items():
            if freq == 1 and n > res:
                res = n

        return res


class Solution2:
    """
    Intuition:
        We can divide the problem into 3 major subcases:

        1. k == N, meaning the whole input array is a single subarray window.
           In this case, we just have to find the maximum value within that
           unique window.

        2. k == 1, meaning each elmt in the input is a window. In this case,
           we have to process each element and select the largest among the
           values that only appear once.

        3. 1 < k < N, meaning we have multiple windows that overlap. The one
           thing to notice here is that in this case, the only possible values
           are the first one (leftmost) and last one (rightmost). We just
           have to ensure they only appear once and return the max.

    Runtime:
        O(n) as each case requires a linear scan.

    Memory:
        O(n) for the counter dictionary.
    """

    def largestInteger(self, nums: List[int], k: int) -> int:
        # case k == n i.e. single subarray window
        if k == len(nums):
            return max(nums)
        # case k == 1 i.e. each elmt is a subarray window
        elif k == 1:
            counter = Counter(nums)
            res = -1

            for n, freq in counter.items():
                if freq == 1 and n > res:
                    res = n

            return res
        # case 1 < k < n i.e. multiple windows
        # only elmts that appear in only 1 subarray are leftmost and rightmost
        else:
            counter = Counter(nums)
            l, r = nums[0], nums[-1]

            if counter[l] == 1 and counter[r] == 1:
                return max(l, r)
            elif counter[l] == 1 and counter[r] > 1:
                return l
            elif counter[l] > 1 and counter[r] == 1:
                return r
            else:
                return -1
