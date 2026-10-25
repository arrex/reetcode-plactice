class Solution:
    """
    Intuition:
        The insight driving our solution is to form a triplet by anchoring the
        middle element and then finding valid a valid elmt to the left and
        another valid elmt to the right.

        We index the BIT with respect to the positioning of elmts in nums2. This
        way, the prefix sum represents the num of elmts appearing before a given
        `n` in both nums1 and nums2.

        We can then derive the num of elmts appearing after `n` in both nums1 and
        nums2. The idea is to take all the elmts we have encountered so far and
        subtract all the ones appearing before `n` in nums1 and nums2 i.e. `ix -
        before` of them and subtract this from the how many elmts are left on the
        right side of pos2 i.e. `N - pos2` elmts.

    Runtime:
        O(n) to build the position hashmap with nums2.

        We have n iterations over nums1. Each iteration costs O(2 * log n) ~ O(log n)
        with the sum and add operation on the BIT. This means a runtime of O(n log n).

        Overall, we have O(n + n * log n) ~ O(n log n) runtime.

    Memory:
        O(n) for the hasmap.

        O(n) for the BIT.

        Overall, O(n) memory.
    """

    class BIT:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)
            self.size = size

        def add(self, ix: int, val: int):
            while ix <= self.size:
                self.bit[ix] += val
                ix += ix & -ix

        def sum(self, ix: int) -> int:
            tot = 0
            while ix > 0:
                tot += self.bit[ix]
                ix -= ix & -ix
            return tot

    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        N = len(nums1)

        # maps num to 1-indexed position in nums2
        posMap = {n: i + 1 for i, n in enumerate(nums2)}

        # init fenwick tree
        bit = self.BIT(N)

        res = 0
        for ix, n1 in enumerate(nums1):
            # find pos of same elmt in nums2
            pos2 = posMap[n1]

            # find all elmts that appear before n1 in both nums1 and nums2
            before = bit.sum(pos2 - 1)
            # find all elmts that appear after n1 in both nums1 and nums2:
            #
            # ix - before counts elmts left of n1 in nums1 but right of n1 in nums2
            # remove these from nums2's right side to count elmts right of n1 in both
            after = (N - pos2) - (ix - before)

            # update fenwick tree
            bit.add(pos2, 1)

            res += before * after

        return res
