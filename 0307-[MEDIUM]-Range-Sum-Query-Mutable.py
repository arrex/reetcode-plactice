class NumArray:
    """
    Intuition:
        This can be solved trivially by persisting aa copy of the nums array
        and calculating range sums via brute force. Updates would happen in
        constant time, but every range sum query would take up to O(n) time
        which is too inefficient for this problem.

        We can use a Fenwick Tree (aka Binary Indexed Tree) to solve this
        problem as it involves efficiently querying range sums and performing
        point updates frequently.

    Runtime:
        init:
            Initializing the nums and fenwick tree arrays takes O(n) time each.

            A single call to _add() requires O(log n) time. We do this n times
            which gives us O(n log n).

        update:
            O(log n) due to the call to _add().

        sumRange:
            Each call to _sum() takes O(log n) time. We perform 2 _sum() calls,
            which yields a runtime of O(2 log n) ~ O(log n).

    Memory:
        O(n) for the nums array that we persist within the class instance.

        O(n) for the fenwick tree array.

        Overall, O(n) memory complexity.
    """

    def __init__(self, nums: list[int]):
        N = len(nums)

        self.size = N
        self.nums = nums
        # adjust to 1-indexed
        self.fenwick = [0] * (N + 1)

        # build fenwick tree
        for i in range(N):
            self._add(i + 1, nums[i])

    # private helper to perform a point update & prop changes
    # to range sums
    def _add(self, ix: int, val: int) -> int:
        while ix <= self.size:
            self.fenwick[ix] += val
            ix += ix & -ix  # add last set bit

    def update(self, ix: int, val: int) -> None:
        delta = val - self.nums[ix]
        self.nums[ix] = val
        self._add(ix + 1, delta)

    # private helper to compute the range sum over nums[0:ix]
    # ix exclusive
    def _sum(self, ix: int) -> int:
        s = 0
        while ix > 0:
            s += self.fenwick[ix]
            ix -= ix & -ix  # flip last set bit

        return s

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
