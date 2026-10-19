from typing import List


class Solution1:
    """
    Intuition:
        We can use a Fenwick tree to store frequencies of numbers. The
        instruction number becomes the index for the Fenwick tree and
        the value stored is its frequency.

        This way, for a given number `n`, the sum of smaller elmts is the
        prefix sum up to index `n - 1`. Similarly, the sum of greater elmts
        is the total amount of instructions we have encountered so far minus
        the number of elmts smaller or equal to the current instruction i.e.
        the prefix sum up to index `n` in the Fenwick tree.

    Runtime:
        Suppose k is the largest elmt in the input array. Initializing the
        Fenwick tree will take O(k) time.

        We have n instructions to process. On each iteration, we call the
        Fenwick tree's add method once, incurring O(log n) runtime. We also
        call the sum method twice, incurring O(2 * log n) ~ O(log n) runtime.
        This leads to a runtime of O(n log n) for the loop.

        Overall, the runtime complexity is O(n log n).

    Memory:
        O(k) for the Fenwick tree.
    """

    class BIT:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)
            self.size = size

        def add(self, ix: int, val: int):
            while ix <= self.size:
                self.bit[ix] += val
                ix += ix & -ix

        def sum(self, ix: int):
            tot = 0
            while ix > 0:
                tot += self.bit[ix]
                ix -= ix & -ix
            return tot

    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7

        # init binary indexed tree
        bit = self.BIT(max(instructions))

        cost = 0
        for i, n in enumerate(instructions):
            # update BIT
            bit.add(n, 1)
            # cost of elmts less than curr
            ltCost = bit.sum(n - 1)
            # cost of elmts greater than curr
            gtCost = (i + 1) - bit.sum(n)
            # update total cost
            cost = (cost + min(ltCost, gtCost)) % MOD

        return cost % MOD


class Solution2:
    """
    Intuition:
        Same as Solution 1.

        However, notice that the num of elmts greater than or equal to the
        current one is `num elmts less than` + `num elmts equal`. We already
        have the num of elmts that are strictly smaller, so we add a freq
        counter to be able to efficiently retrieve the num of elmts equal
        to the current instruction.

    Runtime:
        The big-O runtime is still the same as Solution 1, but performs
        significantly better by removing an extra call to BIT.sum().

    Memory:
        O(k) for the Fenwick tree.

        O(n) for the freq counter.

        Overall, O(n + k) space.
    """

    class BIT:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)
            self.size = size

        def add(self, ix: int, val: int):
            while ix <= self.size:
                self.bit[ix] += val
                ix += ix & -ix

        def sum(self, ix: int):
            tot = 0
            while ix > 0:
                tot += self.bit[ix]
                ix -= ix & -ix
            return tot

    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7

        # init BIT & freq counter
        bit = self.BIT(max(instructions))
        freq = {}

        cost = 0
        for i, n in enumerate(instructions):
            # update BIT & freq counter
            bit.add(n, 1)
            freq[n] = freq.get(n, 0) + 1

            # cost of elmts less than curr
            ltCost = bit.sum(n - 1)
            # cost of elmts greater than curr:
            # (i + 1) = total num of elmts we have seen so far
            # freq[n] = how many elmts w curr value do we have
            # ltCost = how many elmts LT curr value do we have
            gtCost = (i + 1) - freq[n] - ltCost

            # update total cost
            cost = (cost + min(ltCost, gtCost)) % MOD

        return cost % MOD
