from typing import List


class Solution:
    """
    Intuition:
        We can use a sliding window approach here where the size of our window
        is dictated by the number of flipped 0's we have in our window. We know
        we can have at most only k flipped 0's to have a valid window.

        Our solution's algorithm will divide into 3 main cases:
        1) When we hit a 1, we increment curr and check if we have a new max.
        2) When we hit a 0 and the number of flipped 0's is LT k, we can
           flip the current 0 element and count it as if it were a 1.
        3) When we hit a 0 and we have flipped the maximum number of elements
           being k, we need to move the left ptr to clear the leftmost 0 in
           our current window.
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = 0
        l, r = 0, 0
        res, curr = 0, 0

        while r < len(nums):
            if nums[r] == 1:
                curr += 1

                res = max(res, curr)
            else:
                if flipped < k:
                    flipped += 1
                    curr += 1

                    res = max(res, curr)
                else:
                    while nums[l] != 0:
                        curr -= 1
                        l += 1

                    # Do not need to modify flipped or curr
                    # since our newly encountered 0 also counts
                    # towards curr and flipped
                    #
                    # We would decrement to increment again, so
                    # cancels out.
                    l += 1

            r += 1

        return res
