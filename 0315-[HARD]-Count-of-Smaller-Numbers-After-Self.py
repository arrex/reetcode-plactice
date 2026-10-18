class Solution:
    """
    Intuition:
        The brute force approach would be to have a nested loop counting
        smaller elmts to the right which would be O(n^2).

        We need to ask ourselves how to optimize finding the num of smaller
        elmts to the right for each position. We can use a Fenwick Tree to
        do so by storing the frequency of smaller numbers and then summing
        over them.

        To encode ordering, we assign each elmt a slot value. The smallest
        elmt will have slot 1 and the largest will have slot n. This way,
        whenever we encounter an elmt, we simply add a frequency count to
        the slot and update all relevant aggregate sums.

        Then, we process the input array from right to left. Processing in
        this direction makes it such that for every elmt, we have already
        counted all the elmts to its right, so we can simply take the prefix
        sum in the Fenwick Tree.

    Runtime:
        Sorting the input array takes O(n log n) time.

        Building the slot hashmap takes O(n) time.

        Initializing the BIT takes O(n) time.

        The main processing loop takes O(n log n) time as we have n elmts in
        the input array and each requires an add and a sum operation on the
        Fenwick Tree which takes O(log n) time each.

        Then, reversing the list takes O(n) time.

        Overall, the runtime is O(n log n).

    Memory:
        The hashmap takes O(n) space.

        The Fenwick Tree takes O(n) space.

        Overall, O(n) space.
    """

    class BIT:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)
            self.size = size

        def add(self, ix: int, val: int):
            while ix <= self.size:
                self.bit[ix] += val
                ix += ix & -ix  # add last set bit

        def sum(self, ix: int) -> int:
            tot = 0
            while ix > 0:
                tot += self.bit[ix]
                ix -= ix & -ix  # flip last set bit
            return tot

    def countSmaller(self, nums: list[int]) -> list[int]:
        # create a sorted copy of nums
        # then assign each num a 1-indexed slot number
        slotMap = {n: i + 1 for i, n in enumerate(sorted(set(nums)))}

        # init binary indexed tree
        # each slot stores the frequency of the elmt
        # slot 1 = smallest, ..., slot n = largest
        bit = self.BIT(len(slotMap))

        # process nums from right to left since we are interested
        # in how many smaller elmts are TO THE RIGHT of curr position
        res = []
        for n in nums[::-1]:
            # record curr num
            slot = slotMap[n]
            bit.add(slot, 1)

            # sum cnt of smaller elmts
            smallerCnt = bit.sum(slot - 1)  # exclude curr slot from sum
            res.append(smallerCnt)

        # revert to left -> right order
        # since we processed right -> left
        return res[::-1]
